import { Component, Input, OnInit, HostListener } from '@angular/core';
import { ApiService, ChartData } from '../../services/api.service';
import { Subscription } from 'rxjs';
import { environment } from 'src/environments/environment';

interface LatestData {
  name: string,
  timestamp: string,
  total_players: number,
  total_servers: number
}

@Component({
  selector: 'app-statistic',
  templateUrl: './statistic.component.html',
  styleUrls: ['./statistic.component.scss']
})
export class StatisticComponent implements OnInit {
  @Input() public statisticType!: string;
  public statistics = Array();
  public gridListCols = 2;
  public rowHeight!: string;
  public currentTimes = Array();
  public chartData = Object();
  public latestData = Array();

  wsSubscription: Subscription | undefined;
  intervalSubscription: Subscription | undefined;

  constructor(private apiService: ApiService) {
    this.updateGridListCols();
    this.updateRowHeight();
  }

  trackByFn(index: number, config: any): string {
    return `${config.name}`;
  }

  ngOnInit(): void {
    this.wsSubscription = this.apiService.connect(`${environment.WS_URL}/ws/statistics/${this.statisticType}/`)
      .subscribe({
        next: (msgEvent: MessageEvent) => {
          let newData = JSON.parse(msgEvent.data);

          // Handle data going to the live-graph component
          if (!this.chartData[`${newData.name}`]) {
            // set initial data
            this.chartData[`${newData.name}`] = newData.data
          } else {
            // add incoming data
            this.chartData[`${newData.name}`] = [...this.chartData[`${newData.name}`], ...newData.data]

            // remove old data
            const lastElementTimestamp = this.chartData[`${newData.name}`][this.chartData[`${newData.name}`].length - 1].timestamp;
            const oneHourAgoFromLastElement = new Date(lastElementTimestamp);
            oneHourAgoFromLastElement.setHours(oneHourAgoFromLastElement.getHours() - 1);

            this.chartData[`${newData.name}`] = this.chartData[`${newData.name}`].filter((e: ChartData) => {
              return new Date(e.timestamp) >= oneHourAgoFromLastElement;
            });
          }

          // store latest data for component to use
          if (this.latestData.find((e: LatestData) => e.name === newData.name)) {
            this.latestData = this.latestData.map((e: LatestData) => {
              if (e.name === newData.name) {
                let newValues = newData.data[newData.data.length - 1];
                return {
                  ...e,
                  ...newValues,
                  player_difference: newData.data[newData.data.length - 1].total_players - this.chartData[`${newData.name}`][0].total_players,
                  server_difference: newData.data[newData.data.length - 1].total_servers - this.chartData[`${newData.name}`][0].total_servers,
                }
              }
              return e;
            });
          } else {
            this.latestData.push({
              name: newData.name,
              player_difference: newData.data[newData.data.length - 1].total_players - newData.data[0].total_players,
              server_difference: newData.data[newData.data.length - 1].total_servers - newData.data[0].total_servers,
              ...newData.data[newData.data.length - 1]
            })
          }
          
          // sort latest data of highest amount of total players
          this.latestData = this.latestData.sort((a: LatestData, b: LatestData) => b.total_players - a.total_players)
        },
        error: err => console.error('ws error', err),
        complete: () => console.log('ws connection closed')
      });
  }

  ngOnDestroy(): void {
    if (this.wsSubscription) {
      this.wsSubscription.unsubscribe();
    }
    if (this.intervalSubscription) {
      this.intervalSubscription.unsubscribe();
    }
    this.apiService.disconnect();
  }

  getRelativeTime(timestamp: string): string {    
    return `Last updated: ${new Date(timestamp).toLocaleString()}`;
  }

  @HostListener('window:resize', ['$event'])
  onResize() {
    this.updateGridListCols();
  }

  updateGridListCols() {
    // You can add your logic here to update grid list cols
    // based on window.innerWidth for example
    if (window.innerWidth < 600) {
      this.gridListCols = 1;
    } else if (window.innerWidth < 960) {
      this.gridListCols = 2;
    } else {
      this.gridListCols = 3;
    }
  }

  updateRowHeight() {
    // Obtain the first card element
    const cardElement = document.querySelector('.card');
    if (cardElement) {
      // Calculate its height
      const cardHeight = cardElement.clientHeight;

      // You might need to add some extra height to account for padding/margin
      const extraHeight = 20; // adjust as needed
      this.rowHeight = `${cardHeight + extraHeight}px`;
    }
  }

}
