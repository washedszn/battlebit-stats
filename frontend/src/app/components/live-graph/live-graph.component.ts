import { Component, ElementRef, ViewChild, AfterViewInit, OnInit, Input, HostListener } from '@angular/core';
import { Chart, registerables } from 'chart.js';
import { ApiService,  } from 'src/app/services/api.service';
import { tap, Subscription, interval, startWith, switchMap } from 'rxjs';

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
  private subscription!: Subscription;

  constructor(private apiService: ApiService) { }

  ngOnInit() {    
    this.subscription = interval(5_000) // Emit a value every 5 seconds
      .pipe(
        startWith(0),
        switchMap(() => this.apiService.getLiveData(this.statisticType, this.filter)),
        tap((data: any[]) => {
          if (!this.chart.data.labels!.length && !this.chart.data.datasets[0].data.length) {
            // This is the first batch of data, use it to initialize the chart
            // Reverse the data as the chart plots from oldest to newest
            data = data.reverse();
            this.chart.data.labels = data.map(item => `${new Date(item.timestamp).toLocaleString()} - Total Players: ${item.total_players}`);
            this.chart.data.datasets[0].data = data.map(item => item.total_players);
          } else {
            // Chart is already initialized, just add new data and remove old one
            const item = data[0];
            const newLabel = `${new Date(item.timestamp).toLocaleString()} - Total Players: ${item.total_players}`;
            const newDataPoint = item.total_players;
  
            // Remove the first element (oldest data point)
            this.chart.data.labels!.shift();
            this.chart.data.datasets[0].data.shift();
  
            // Add the new data to the end
            this.chart.data.labels!.push(newLabel);
            this.chart.data.datasets[0].data.push(newDataPoint);
          }
  
          this.chart.update('none'); // Update chart without animating
        })
      )
      .subscribe();
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

  ngAfterViewInit() {
    this.createChart();
    this.resizeChart();
  }

  createChart() {
    this.chart = new Chart(this.chartCanvas.nativeElement, {
      type: 'line',
      data: {
        labels: [],
        datasets: [{
          label: 'Total Players',
          data: [],
          fill: false,
          pointRadius: 0,
          pointHitRadius: 0,
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
            display: false
          }
        },
        responsive: true,
        maintainAspectRatio: true
      }
    });
  }

  resizeChart() {
    if (this.chart.canvas.parentNode != null) {
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
