import { Component } from '@angular/core';
import { Meta, Title } from '@angular/platform-browser';

@Component({
  selector: 'app-game-modes',
  templateUrl: './game-modes.component.html',
  styleUrls: ['./game-modes.component.scss']
})
export class GameModesComponent {
  constructor(private metaTagService: Meta, private titleService: Title) { }

  ngOnInit() {
    this.titleService.setTitle('BattleBitStats - Game Mode Statistics');

    this.metaTagService.addTags([
      { name: 'description', content: 'Real-time statistics for different game modes in BattleBit Remastered.' },
      { property: 'og:url', content: 'https://battlebitstats.xyz/game-modes' },
      { property: 'og:title', content: 'BattleBitStats - Game Mode Statistics' },
      { property: 'og:description', content: 'Real-time statistics for different game modes in BattleBit Remastered.' },
      { property: 'og:image', content: 'https://battlebitstats.xyz/assets/images/game-modes.png' },
      { name: 'twitter:card', content: 'summary_large_image' },
      { name: 'twitter:title', content: 'BattleBitStats - Game Mode Statistics' },
      { name: 'twitter:description', content: 'Real-time statistics for different game modes in BattleBit Remastered.' },
      { name: 'twitter:image', content: 'https://battlebitstats.xyz/assets/images/game-modes.png' },
    ]);
  }
}
