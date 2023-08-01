import { Component, ElementRef, ViewChild, AfterViewInit, Input, OnChanges, SimpleChanges, HostListener } from '@angular/core';
import { Chart, registerables } from 'chart.js';
import { BarChartData } from 'src/app/services/api.service';
import { eachHourOfInterval, format } from 'date-fns';
import 'chartjs-adapter-date-fns';

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
    this.chart = new Chart(this.chartCanvas.nativeElement, {
      type: 'bar',
      data: {
        labels: this.chartData.timestamps.map((e) => {
          const timestampDate = new Date(e as string);
          return timestampDate.toLocaleString();
        }),
        datasets: [{
          label: 'Min & Max player count',
          data: this.chartData.min_players.map((min, index) => {
            return [min, this.chartData.max_players[index]];
          }),
          backgroundColor: 'rgb(75, 192, 192)',
          borderColor: 'rgb(75, 192, 192)',
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
          y: {
            beginAtZero: false,
          },
        },
        responsive: true,
        maintainAspectRatio: true,
      }
    });
  }

  updateChart() {
    if (!this.chartData) return;
  
    // Create the chart instance if it does not exist
    if (!this.chart) {
      this.createChart();
    }
  
    // Update chart data and labels
    this.chart.data.labels = this.chartData.timestamps.map((e) => {
      const timestampDate = new Date(e as string);
      return timestampDate.toLocaleString();
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
