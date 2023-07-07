import { Component, ElementRef, ViewChild, AfterViewInit, OnInit, Input, HostListener } from '@angular/core';
import { Chart, registerables } from 'chart.js';
import { ApiService } from 'src/app/services/api.service';
import { EMPTY, Subscription, interval, startWith, switchMap } from 'rxjs';

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
    this.subscription = interval(60_000) // Emit a value every 60 seconds (1 minute)
      .pipe(
        startWith(0),
        switchMap(() => {
          return this.apiService.getLiveData(this.statisticType, this.filter)
            .pipe(
              switchMap((data: any[]) => {
                console.log('Data from API:', data);

                data.forEach((item: any) => {
                  const label = `${new Date(item.timestamp).toLocaleString()} - Total Players: ${item.total_players}`;
                  const newDataPoint = item.total_players;

                  console.log('Label:', label);
                  console.log('New Data Point:', newDataPoint);

                  this.chart.data.labels!.push(label);
                  this.chart.data.datasets[0].data.push(newDataPoint);
                });

                const maxDataPoints = 60;
                while (this.chart.data.labels!.length > maxDataPoints) {
                  this.chart.data.labels!.shift();
                  this.chart.data.datasets[0].data.shift();
                }

                this.chart.update();
                //this.resizeChart();

                return EMPTY;
              })
            );
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
