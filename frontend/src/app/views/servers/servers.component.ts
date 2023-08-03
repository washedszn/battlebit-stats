import { Component } from '@angular/core';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { Meta, Title } from '@angular/platform-browser';
import { BarChartData, ApiService } from 'src/app/services/api.service';
import { Subscription, Subject, interval, merge } from 'rxjs';
import { startWith, switchMap } from 'rxjs/operators';

@Component({
  selector: 'app-servers',
  templateUrl: './servers.component.html',
  styleUrls: ['./servers.component.scss']
})
export class ServersComponent {
  form!: FormGroup;
  private subscription!: Subscription;
  public chartData = Array<BarChartData>();
  datetimeRange = '';
  private dataRefreshTrigger = new Subject<void>();

  constructor(private metaTagService: Meta, private titleService: Title, private apiService: ApiService, private fb: FormBuilder) { }

  ngOnInit() {
    this.form = this.fb.group({
      datetime: ['']
    });

    // Create an observable that emits a value every 60 seconds
    const interval$ = interval(60_000).pipe(startWith(0));

    // Merge the interval observable with the subject
    const merged$ = merge(this.dataRefreshTrigger, interval$);

    this.subscription = merged$.pipe(
      switchMap(() => this.apiService.getPlayerStatistics(this.datetimeRange))
    ).subscribe({
      next: (data) => {
        data.sort((a: BarChartData, b: BarChartData) => {
          const maxA = Math.max(...a.max_players);
          const maxB = Math.max(...b.max_players);
          return maxB - maxA; // this will sort in descending order
        });        
        this.chartData = data;
      }
    })

    this.titleService.setTitle('BattleBitStats - Server Statistics');
  
    this.metaTagService.addTags([
      {name: 'description', content: 'Real-time statistics for servers in BattleBit Remastered.'},
      {property: 'og:url', content: 'https://battlebitstats.xyz/home'},
      {property: 'og:title', content: 'BattleBitStats - Server Statistics'},
      {property: 'og:description', content: 'Real-time statistics for servers in BattleBit Remastered.'},
      {property: 'og:image', content: 'https://battlebitstats.xyz/assets/images/general.png'},
      {name: 'twitter:card', content: 'summary_large_image'},
      {name: 'twitter:title', content: 'BattleBitStats - Server Statistics'},
      {name: 'twitter:description', content: 'Real-time statistics for servers in BattleBit Remastered.'},
      {name: 'twitter:image', content: 'https://battlebitstats.xyz/assets/images/general.png'},
    ]);

    this.refreshData();  // Call this to trigger the initial data load
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }

  trackByFn(index: number, config: any): string {
    return `${config.name}`;
  }

  onDateTimeSelected(range: {start: string, end: string}): void {
    this.datetimeRange = `${range.start} 00:00:00/${range.end} 23:00:00`;    
    this.refreshData();  // Call this to refresh the data when the datetime changes
  }

  // Call this method to trigger a data refresh
  refreshData(): void {
    this.dataRefreshTrigger.next();
  }
}
