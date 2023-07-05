import { Component, Input, OnInit } from '@angular/core';
import { ChartDataset, ChartOptions, ChartType } from 'chart.js';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-live-graph',
  templateUrl: './live-graph.component.html',
  styleUrls: ['./live-graph.component.scss']
})
export class LiveGraphComponent implements OnInit {
  @Input() statisticType!: string;
  @Input() filter!: string;
  public lineChartData: ChartDataset[] = [{ data: [], label: 'Live Data' }];
  public lineChartLabels: string[] = [];

  public lineChartOptions: (ChartOptions) = {
    responsive: true,
  };

  public lineChartColors = [
    {
      borderColor: 'black',
      backgroundColor: 'rgba(255,0,0,0.3)',
    },
  ];

  public lineChartLegend = true;
  public lineChartType: ChartType = 'line';
  public lineChartPlugins = [];

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.updateChart();
    setInterval(() => {
      this.updateChart();
    }, 5000); // Updates every 5 seconds
  }
  
  updateChart() {
    // Fetch data from API and update this.lineChartData and this.lineChartLabels
    this.apiService.getLiveData(this.statisticType, this.filter).subscribe((data: any) => {
      this.lineChartData[0].data = data.values;
      this.lineChartLabels = data.labels;
    });
  }
}
