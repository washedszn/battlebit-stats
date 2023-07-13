import { Component } from '@angular/core';
import { Meta, Title } from '@angular/platform-browser';

@Component({
  selector: 'app-map-sizes',
  templateUrl: './map-sizes.component.html',
  styleUrls: ['./map-sizes.component.scss']
})
export class MapSizesComponent {
  constructor(private metaTagService: Meta, private titleService: Title) { }

  ngOnInit() {
    this.titleService.setTitle('BattleBitStats - Map Size Statistics');

    this.metaTagService.addTags([
      { name: 'description', content: 'Real-time statistics for different map sizes in BattleBit Remastered.' },
      { property: 'og:url', content: 'https://battlebitstats.xyz/map-sizes' },
      { property: 'og:title', content: 'BattleBitStats - Map Size Statistics' },
      { property: 'og:description', content: 'Real-time statistics for different map sizes in BattleBit Remastered.' },
      { property: 'og:image', content: 'https://battlebitstats.xyz/assets/images/map-sizes.png' },
      { name: 'twitter:card', content: 'summary_large_image' },
      { name: 'twitter:title', content: 'BattleBitStats - Map Size Statistics' },
      { name: 'twitter:description', content: 'Real-time statistics for different map sizes in BattleBit Remastered.' },
      { name: 'twitter:image', content: 'https://battlebitstats.xyz/assets/images/map-sizes.png' },
    ]);
  }
}
