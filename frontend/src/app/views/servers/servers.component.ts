import { Component } from '@angular/core';
import { Meta, Title } from '@angular/platform-browser';
import { BarChartData, ApiService } from 'src/app/services/api.service';
import { Subscription, interval, startWith, switchMap } from 'rxjs';

@Component({
  selector: 'app-servers',
  templateUrl: './servers.component.html',
  styleUrls: ['./servers.component.scss']
})
export class ServersComponent {
  private subscription!: Subscription;
  public chartData = Array<BarChartData>();

  constructor(private metaTagService: Meta, private titleService: Title, private apiService: ApiService) { }

  ngOnInit() {
    this.subscription = interval(60_000).pipe(
      startWith(0),
      switchMap(() => this.apiService.getPlayerStatistics())
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
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }

  trackByFn(index: number, config: any): string {
    return `${config.name}`;
  }
}
