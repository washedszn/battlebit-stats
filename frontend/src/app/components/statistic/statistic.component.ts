import { Component, Input, OnInit, HostListener } from '@angular/core';
import { ApiService, LatestBatch } from '../../services/api.service';
import { Subscription } from 'rxjs';

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

  private subscription!: Subscription;

  constructor(private apiService: ApiService) {
    this.updateGridListCols();
    this.updateRowHeight();
  }

  ngOnInit(): void {
    this.getStatistics();
    setInterval(() => {
      this.getStatistics();
    }, 60_000); // Updates every 60 seconds
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe(); // this will prevent memory leaks
  }

  getStatistics() {
    this.subscription = this.apiService.getStatistics(this.statisticType).subscribe({
      next: (data) => {
        this.statistics = data.sort((a: LatestBatch, b: LatestBatch) => b.total_players - a.total_players);
      },
      error: (error) => {
        console.error('Error: ', error);
      }
    });
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
