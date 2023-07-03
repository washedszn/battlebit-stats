import { Component, OnInit } from '@angular/core';
import { ServerStatsService } from '../../services/server-stats.service';

@Component({
  selector: 'app-server-stats',
  templateUrl: './server-stats.component.html',
  styleUrls: ['./server-stats.component.scss']
})
export class ServerStatsComponent implements OnInit {
  serverStats: any;

  constructor(private serverStatsService: ServerStatsService) { }

  ngOnInit() {
    this.getServerStats();
  }

  getServerStats(): void {
    this.serverStatsService.getServerStats().subscribe(stats => this.serverStats = stats);
  }
}
