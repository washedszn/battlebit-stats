import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-datetime-range-picker',
  templateUrl: './datetime-range-picker.component.html',
  styleUrls: ['./datetime-range-picker.component.scss']
})
export class DatetimeRangePickerComponent implements OnInit {
  public minEndDate!: Date;
  public maxEndDate!: Date;

  @Output() dateTimeSelected: EventEmitter<{ start: string, end: string }> = new EventEmitter<{ start: string, end: string }>();

  start = new FormControl<Date | null>(null);
  end = new FormControl<Date | null>(null);

  endDateFilter = (d: Date | null): boolean => {
    const date = d || new Date();
    // We allow the end date to be selected if it's within the min and max end dates.
    return date >= this.minEndDate && date <= this.maxEndDate;
  };

  constructor() { }

  ngOnInit(): void {
    const now = new Date();
    const yesterday = new Date(now);
    yesterday.setDate(yesterday.getDate() - 1);
    this.start.setValue(yesterday);

    // Set initial end date as tomorrow
    const tomorrow = new Date(now);
    tomorrow.setDate(tomorrow.getDate() + 1);
    this.end.setValue(tomorrow);

    // Set initial min and max end dates
    this.minEndDate = tomorrow;
    const nextWeek = new Date(yesterday);
    nextWeek.setDate(nextWeek.getDate() + 7);
    this.maxEndDate = nextWeek;

    this.start.valueChanges.subscribe(val => {      
      if (val) {
        this.end.setValue(null); // clear end date when start date changes
        const maxEndDate = new Date(val);
        maxEndDate.setDate(maxEndDate.getDate() + 7);
        const minEndDate = new Date(val);
        minEndDate.setDate(minEndDate.getDate() + 1);

        this.minEndDate = minEndDate;
        this.maxEndDate = maxEndDate;
      }
    });

    this.end.valueChanges.subscribe(val => {
      this.updateValue();
    });
  }

  updateValue(): void {
    const start = this.start.value;
    const end = this.end.value;
    
    if (start && end) {
      const startUTC = this.formatDatetime(start);
      const endUTC = this.formatDatetime(end);

      this.dateTimeSelected.emit({ start: startUTC, end: endUTC });
    }
  }

  private formatDatetime(date: Date): string {
    if (date) {
      const year = date.getUTCFullYear();
      const month = ('0' + (date.getUTCMonth() + 1)).slice(-2);
      const day = ('0' + date.getUTCDate()).slice(-2);
      return `${year}-${month}-${day}`;
    } else {
      // Handle null or undefined date here.
      console.error('Received null or undefined date.');
      return '';
    }
  }
}
