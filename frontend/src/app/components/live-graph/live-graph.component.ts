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

  constructor() { }

  ngOnChanges(changes: SimpleChanges) {
    if (changes['chartData'] && changes['chartData'].currentValue) {
      const newChartData = changes['chartData'].currentValue;
      if (this.chart) {
        this.chart.data.labels = newChartData.map((e: ChartData) => e.timestamp);
        this.chart.data.datasets[0].data = newChartData.map((e: ChartData) => {
          return {
            x: new Date(e.timestamp).getTime(),
            y: e.total_players
          }
        });
        this.chart.update('none');                    
      }
    }
  }

  ngAfterViewInit() {
    this.createChart();
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
          fill: false,
          pointRadius: 0,
          pointHitRadius: 0,
          borderColor: 'rgb(75, 192, 192)',
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
          },
          decimation: {
            algorithm: 'min-max',
            enabled: true,
            //samples: 300,
          }
        },
        scales: {
          x: {
            display: false,
            type: 'time',
          }
        },
        responsive: true,
        maintainAspectRatio: true
      }
    });
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
