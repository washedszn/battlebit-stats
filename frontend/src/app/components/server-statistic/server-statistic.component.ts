import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api.service';
import { Subscription, interval, startWith, switchMap } from 'rxjs';

@Component({
  selector: 'app-server-statistic',
  templateUrl: './server-statistic.component.html',
  styleUrls: ['./server-statistic.component.scss']
})
export class ServerStatisticComponent implements OnInit {
  public data: any;
  public oldData: any;
  
  private subscription!: Subscription;

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.subscription = interval(5000).pipe( // Update every 5 seconds
      startWith(0),
      switchMap(() => this.apiService.getStatistics('aggregatedserverstatistics'))
    ).subscribe({
      next: (data) => {
        this.data = data[0];
        this.oldData = data[0];
      }
    })
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe(); // this will prevent memory leaks
  }

  getRelativeTime(timestamp: string): string {
    return `Last updated: ${new Date(timestamp).toLocaleString()}`;
  }
}
