import { Component, ElementRef, ViewChild, AfterViewInit, OnInit, Input } from '@angular/core';
import { Chart, registerables } from 'chart.js';
import { ApiService, ChartData } from 'src/app/services/api.service';

Chart.register(...registerables);

@Component({
  selector: 'app-live-graph',
  templateUrl: './live-graph.component.html',
  styleUrls: ['./live-graph.component.scss']
})
export class LiveGraphComponent implements AfterViewInit, OnInit {
  @ViewChild('chartCanvas') chartCanvas!: ElementRef<HTMLCanvasElement>;
  @Input() public statisticType!: string;
  @Input() public filter!: string;
  public chart!: Chart;

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.updateChart();
    setInterval(() => {
      this.updateChart();
    }, 60_000); // Updates every 60 seconds
  }

  ngAfterViewInit() {
    this.chart = new Chart(this.chartCanvas.nativeElement, {
      type: 'line',
      data: {
        labels: [], // your labels here
        datasets: [{
          label: 'Total Players',
          data: [], // your data here
          fill: false,
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.3,
        }]
      },
      options: {
        plugins: {
          legend: {
            display: false
          }
        },
        scales: {
          x: {
            display: false // Hide X axis labels
          }
        },
      }
    });
  }

  updateChart() {
    // Fetch data from API and update this.lineChartData and this.lineChartLabels
    this.apiService.getLiveData(this.statisticType, this.filter).subscribe((data: any) => {
      const labels = data.map((e: ChartData) => `${new Date(e.timestamp).toLocaleString()} - Total Players: ${e.total_players}`);
      const datasetData = data.map((e: ChartData) => e.total_players);

      this.chart.data.labels = labels;
      this.chart.data.datasets[0].data = datasetData;

      this.chart.update();
    });
  }
}
