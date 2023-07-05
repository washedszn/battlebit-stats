import { Component, Input, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-statistic',
  templateUrl: './statistic.component.html',
  styleUrls: ['./statistic.component.scss']
})
export class StatisticComponent implements OnInit {
  @Input() statisticType!: string;
  statistics: any;

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.apiService.getStatistics(this.statisticType).subscribe(
      (data) => {
        this.statistics = data;
      },
      (error) => {
        console.error('Error: ', error);
      }
    );
  }
}
