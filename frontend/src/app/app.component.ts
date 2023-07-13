import { Component } from '@angular/core';
import { Meta, Title } from '@angular/platform-browser';
import { BreakpointObserver } from '@angular/cdk/layout';
import { Observable } from 'rxjs';
import { map, shareReplay } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  isSmallScreen$!: Observable<boolean>;

  constructor(private metaTagService: Meta, private titleService: Title, private breakpointObserver: BreakpointObserver) { }

  ngOnInit() {
    this.isSmallScreen$ = this.breakpointObserver.observe(['(max-width: 650px)'])
    .pipe(
      map(result => result.matches),
      shareReplay()
    );

    this.titleService.setTitle('BattleBitStats - Real-time Statistics for BattleBit Remastered');
  
    this.metaTagService.addTags([
      {name: 'keywords', content: 'BattleBit, Statistics, BattleBit Remastered, Gaming, PC Game, Real-time Stats'},
      {name: 'description', content: 'BattleBitStats provides real-time statistics for BattleBit Remastered game servers.'},
      {name: 'robots', content: 'index, follow'},
      {name: 'author', content: 'washedszn'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'},
      {name: 'date', content: '2023-07-13', scheme: 'YYYY-MM-DD'},
      {charset: 'UTF-8'}
    ]);
  }
}
