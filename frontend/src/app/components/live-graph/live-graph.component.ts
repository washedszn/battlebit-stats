import { Component, ElementRef, ViewChild, AfterViewInit, Input, OnChanges, SimpleChanges, HostListener } from '@angular/core';
import { Chart, registerables } from 'chart.js';
import { ChartData } from 'src/app/services/api.service';
import 'chartjs-adapter-date-fns';

Chart.register(...registerables);

@Component({
  selector: 'app-live-graph',
  templateUrl: './live-graph.component.html',
  styleUrls: ['./live-graph.component.scss']
})
export class LiveGraphComponent implements AfterViewInit, OnChanges {
  @ViewChild('chartCanvas') chartCanvas!: ElementRef<HTMLCanvasElement>;
  @Input() public chartData = Array<ChartData>();
  public chart!: Chart;

  public timeRange: number = 60 * 10 * 1000; // Default to 10 minutes

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
      type: 'line',
      data: {
        datasets: [{
          label: 'Total Players',
          data: this.chartData.map((e: ChartData) => {
            return {
              x: new Date(e.timestamp).getTime(),
              y: e.total_players
            }
          }),
          fill: true,
          pointRadius: 0,
          pointHitRadius: 0,
          borderColor: 'rgb(75, 192, 192)',
          backgroundColor: 'rgba(75, 192, 192, 0.1)',
          borderCapStyle: 'round',
          tension: 0.2,
          stepped: false,
          borderDash: []
        }]
      },
      options: {
        spanGaps: true,
        normalized: true,
        animation: false,
        parsing: false,
        plugins: {
          legend: {
            display: false
          }
        },
        scales: {
          x: {
            display: false,
            type: 'time',
            grid: {
              display: false
            }
          },
          y: {
            grid: {
              display: false
            }
          }
        },
        responsive: true,
        maintainAspectRatio: true
      }
    });
  }

  updateChart() {
    if (!this.chartData || this.chartData.length === 0) return;
  
    const sortedData = [...this.chartData].sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime());
    const latestTimestamp = new Date(sortedData[0].timestamp).getTime();
  
    const filteredData = sortedData.filter((e: ChartData) =>
      latestTimestamp - new Date(e.timestamp).getTime() <= this.timeRange
    );
  
    this.chart.data.labels = filteredData.map((e: ChartData) => e.timestamp);
    this.chart.data.datasets[0].data = filteredData.map((e: ChartData) => {
      return {
        x: new Date(e.timestamp).getTime(),
        y: e.total_players
      }
    });
  
    // Get the max y value in the dataset
    const maxY = Math.max(...filteredData.map(e => e.total_players));
  
    // Add a 10% padding to the max y value
    const suggestedMax = maxY + maxY * 0.01;
  
    // Check if this.chart is defined and then set the new suggestedMax value for the chart
    if (this.chart && this.chart.options && this.chart.options.scales && this.chart.options.scales['y']) {
      (this.chart.options.scales['y'] as any).suggestedMax = suggestedMax;
    }
  
    this.chart.update('none');
  }

  setTimeRange(range: number) {
    this.timeRange = range;
    this.updateChart();
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
