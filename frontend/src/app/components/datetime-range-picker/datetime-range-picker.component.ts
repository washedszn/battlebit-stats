import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-datetime-range-picker',
  templateUrl: './datetime-range-picker.component.html',
  styleUrls: ['./datetime-range-picker.component.scss']
})
export class DatetimeRangePickerComponent implements OnInit {

  @Output() dateTimeSelected: EventEmitter<{ start: string, end: string }> = new EventEmitter<{ start: string, end: string }>();

  range = new FormGroup({
    start: new FormControl<Date | null>(null),
    end: new FormControl<Date | null>(null),
  });
  maxEndDate!: Date;
  minEndDate!: Date;

  constructor() { }

  ngOnInit(): void {
    const now = new Date();
    const yesterday = new Date(now);
    yesterday.setDate(yesterday.getDate() - 1);
  
    this.range.setValue({ start: yesterday, end: now });
  
    this.range.get('start')?.valueChanges.subscribe(val => {      
      if (val) {
        const maxEndDate = new Date(val);
        maxEndDate.setDate(maxEndDate.getDate() + 7);
        const minEndDate = new Date(val);
        minEndDate.setDate(minEndDate.getDate() + 1);

        this.minEndDate = minEndDate;
        this.maxEndDate = maxEndDate;
      }
    });
  }

  updateValue() {
    const start = this.range.get('start')?.value;
    const end = this.range.get('end')?.value;
    
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
