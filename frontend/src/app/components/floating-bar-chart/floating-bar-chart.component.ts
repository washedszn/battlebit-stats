import { Component, ElementRef, ViewChild, AfterViewInit, Input, OnChanges, SimpleChanges, HostListener } from '@angular/core';
import { Chart, registerables } from 'chart.js';
import { BarChartData } from 'src/app/services/api.service';

Chart.register(...registerables);

@Component({
  selector: 'app-floating-bar-chart',
  templateUrl: './floating-bar-chart.component.html',
  styleUrls: ['./floating-bar-chart.component.scss']
})
export class FloatingBarChartComponent implements AfterViewInit, OnChanges {
  @ViewChild('chartCanvas') chartCanvas!: ElementRef<HTMLCanvasElement>;
  @Input() public chartData!: BarChartData;
  public chart!: Chart;

  constructor() { }

  ngOnChanges(changes: SimpleChanges) {
    if (changes['chartData'] && changes['chartData'].currentValue) {
      this.updateChart();
    }
  }

  ngAfterViewInit() {
    this.createChart();
    this.updateChart();
    this.resizeChart();
  }

  createChart() {
    if (!this.chartCanvas) {
      console.log('Cannot create chart because canvas is not available yet');
      return;
    }

    this.chart = new Chart(this.chartCanvas.nativeElement, {
      type: 'bar',
      data: {
        labels: this.chartData.timestamps.map(e => {          
          return new Date(e)
        }),
        datasets: [{
          label: 'Min & Max player count',
          data: this.chartData.min_players.map((min, index) => {
            return [min, this.chartData.max_players[index]];
          }),
          borderColor: 'rgb(75, 192, 192)',
          backgroundColor: 'rgba(75, 192, 192, 0.1)',
          borderWidth: 2,
          borderRadius: 4,
          borderSkipped: false,

        }]
      },
      options: {
        indexAxis: 'x',
        plugins: {
          legend: {
            display: false
          },
          tooltip: {
            callbacks: {
              title: function (context) {
                const index = context[0]?.dataIndex;
                const labels = context[0]?.chart?.data?.labels;
                
                return `At ${labels?.[index]}, the player peaks were:`;
              },
              label: function (context) {
                const dataset = context.dataset;
                const index = context.dataIndex;
                if (Array.isArray(dataset.data[index])) {
                  const values = dataset.data[index] as [number, number];
                  return `Minimum: ${values[0].toLocaleString()}, Maximum: ${values[1].toLocaleString()}`;
                } else {
                  return '';
                }
              }
            }
          }
        },
        scales: {
          x: {
            ticks: {
              autoSkip: true,
              callback: function(value, index, values) {
                // Check if `this.chart` and its properties are defined
                if (!this || !this.chart || !this.chart.data || !this.chart.data.labels) {
                  return null;
                }
              
                // Access the original date value from your data
                const date = new Date(this.chart.data.labels[index] as string);
              
                // Get the previous date value if it exists
                const previousDate = index > 0 ? new Date(this.chart.data.labels[index - 1] as string) : null;
              
                // Only return the label for the first index, the last index, and when the day changes
                if (index === 0 || index === this.chart.data.labels.length - 1 || !previousDate || date.getDate() !== previousDate.getDate()) {
                  // Format the date as "DD-MM HH:mm"
                  const day = ('0' + date.getDate()).slice(-2);
                  const month = ('0' + (date.getMonth() + 1)).slice(-2);
                  const hours = ('0' + date.getHours()).slice(-2);
                  const minutes = ('0' + date.getMinutes()).slice(-2);
              
                  return `${day}-${month} ${hours}:${minutes}`;
                }
              
                // Return null for other labels
                return null;
              }              
            }
          },
          y: {
            beginAtZero: false,
            grid: {
              display: true
            }
          },
        },
        responsive: true,
        maintainAspectRatio: true,
      }
    });
  }

  updateChart() {
    if (!this.chartData || !this.chartCanvas) return;

    // Create the chart instance if it does not exist
    if (!this.chart) {
      this.createChart();
    }

    // Update chart data and labels
    this.chart.data.labels = this.chartData.timestamps.map((e) => {    
      return new Date(e)
    });
    this.chart.data.datasets[0].data = this.chartData.min_players.map((min, index) => {
      return [min, this.chartData.max_players[index]];
    });

    // Update the chart
    this.chart.update('none');
  }

  resizeChart() {
    if (this.chart && this.chart.canvas && this.chart.canvas.parentNode != null) {
      (this.chart.canvas.parentNode as HTMLElement).style.height = 'auto';
      (this.chart.canvas.parentNode as HTMLElement).style.width = 'auto';
      this.chart.resize();
    }
  }

  @HostListener('window:resize', ['$event'])
  onResize(event: any) {
    this.resizeChart();
  }
}
