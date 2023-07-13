import { Component } from '@angular/core';
import { Meta, Title } from '@angular/platform-browser';

@Component({
  selector: 'app-regions',
  templateUrl: './regions.component.html',
  styleUrls: ['./regions.component.scss']
})
export class RegionsComponent {
  constructor(private metaTagService: Meta, private titleService: Title) { }

  ngOnInit() {
    this.titleService.setTitle('BattleBitStats - Region Statistics');

    this.metaTagService.addTags([
      { name: 'description', content: 'Real-time statistics for different regions in BattleBit Remastered.' },
      { property: 'og:url', content: 'https://battlebitstats.xyz/regions' },
      { property: 'og:title', content: 'BattleBitStats - Region Statistics' },
      { property: 'og:description', content: 'Real-time statistics for different regions in BattleBit Remastered.' },
      { property: 'og:image', content: 'https://battlebitstats.xyz/assets/images/regions.png' },
      { name: 'twitter:card', content: 'summary_large_image' },
      { name: 'twitter:title', content: 'BattleBitStats - Region Statistics' },
      { name: 'twitter:description', content: 'Real-time statistics for different regions in BattleBit Remastered.' },
      { name: 'twitter:image', content: 'https://battlebitstats.xyz/assets/images/regions.png' },
    ]);
  }
}
