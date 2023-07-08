import { Component, Input, OnInit, HostListener  } from '@angular/core';
import { ApiService, LatestBatch } from '../../services/api.service';
import { Subscription, interval, startWith, switchMap } from 'rxjs';
import { DateTime } from "luxon";

@Component({
  selector: 'app-statistic',
  templateUrl: './statistic.component.html',
  styleUrls: ['./statistic.component.scss']
})
export class StatisticComponent implements OnInit {
  @Input() public statisticType!: string;
  public statistics: any;
  public gridListCols = 2;
  public rowHeight!: string;
  public currentTimes = Array();
  public oldStatistics = Array();

  private subscription!: Subscription;

  constructor(private apiService: ApiService) {
    this.updateGridListCols();
    this.updateRowHeight();
  }

  trackByFn(index: number, config: any): string {
    return `${config.name}`;
  }

  ngOnInit(): void {
    this.subscription = interval(5000).pipe( // Update every 5 seconds
      startWith(0),
      switchMap(() => this.apiService.getStatistics(this.statisticType))
    ).subscribe({
      next: (data) => {        
        this.statistics = data.sort((a: LatestBatch, b: LatestBatch) => b.total_players - a.total_players);
        data.forEach((element: LatestBatch, i: number) => {
          let timezone = this.mapFilterToTimezone(element.name)
          this.currentTimes[i] = DateTime.now().setZone(timezone).toLocaleString(DateTime.TIME_24_SIMPLE);
        });
        this.oldStatistics = data;
      },
      error: (error) => {
        console.error('Error: ', error);
      }
    });
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe(); // this will prevent memory leaks
  }

  mapFilterToTimezone(filter: string): string {
    const map: Record<string, string> = {
      'Japan_Central': 'Asia/Tokyo',
      'America_Central': 'America/Chicago',
      'Brazil_Central': 'America/Sao_Paulo',
      'Europe_Central': 'Europe/Paris',
      'Australia_Central': 'Australia/Sydney'
    };
  
    return map[filter] || 'UTC'; // Default to UTC if the filter isn't found in the map
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
