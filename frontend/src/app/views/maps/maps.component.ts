import { Component } from '@angular/core';
import { Meta, Title } from '@angular/platform-browser';

@Component({
  selector: 'app-maps',
  templateUrl: './maps.component.html',
  styleUrls: ['./maps.component.scss']
})
export class MapsComponent {
  constructor(private metaTagService: Meta, private titleService: Title) { }

  ngOnInit() {
    this.titleService.setTitle('BattleBitStats - Map Statistics');

    this.metaTagService.addTags([
      { name: 'description', content: 'Real-time statistics for different maps in BattleBit Remastered.' },
      { property: 'og:url', content: 'https://battlebitstats.xyz/map' },
      { property: 'og:title', content: 'BattleBitStats - Map Statistics' },
      { property: 'og:description', content: 'Real-time statistics for different maps in BattleBit Remastered.' },
      { property: 'og:image', content: 'https://battlebitstats.xyz/assets/images/maps.png' },
      { name: 'twitter:card', content: 'summary_large_image' },
      { name: 'twitter:title', content: 'BattleBitStats - Map Statistics' },
      { name: 'twitter:description', content: 'Real-time statistics for different maps in BattleBit Remastered.' },
      { name: 'twitter:image', content: 'https://battlebitstats.xyz/assets/images/maps.png' },
    ]);
  }
}
