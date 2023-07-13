import { Component } from '@angular/core';
import { Meta, Title } from '@angular/platform-browser';

@Component({
  selector: 'app-servers',
  templateUrl: './servers.component.html',
  styleUrls: ['./servers.component.scss']
})
export class ServersComponent {
  constructor(private metaTagService: Meta, private titleService: Title) { }

  ngOnInit() {
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
}
