import { Component, OnInit, AfterViewInit, Output, EventEmitter, forwardRef } from '@angular/core';
import { NG_VALUE_ACCESSOR, ControlValueAccessor } from '@angular/forms';

@Component({
  selector: 'app-datetime-range-picker',
  templateUrl: './datetime-range-picker.component.html',
  styleUrls: ['./datetime-range-picker.component.scss'],
  providers: [
    {
      provide: NG_VALUE_ACCESSOR,
      useExisting: forwardRef(() => DatetimeRangePickerComponent),
      multi: true
    }
  ]
})
export class DatetimeRangePickerComponent implements OnInit, ControlValueAccessor {

  @Output() dateTimeSelected: EventEmitter<{start: string, end: string}> = new EventEmitter<{start: string, end: string}>();

  datetimeRange = { start: '', end: '' };

  constructor() { }

  ngOnInit(): void {
    const now = new Date();
    const year = now.getFullYear();
    const month = ('0' + (now.getMonth() + 1)).slice(-2);
    const day = ('0' + now.getDate()).slice(-2);
    const hour = ('0' + now.getHours()).slice(-2);
    
    const yesterday = new Date(now);
    yesterday.setDate(yesterday.getDate() - 1);
    const startYear = yesterday.getFullYear();
    const startMonth = ('0' + (yesterday.getMonth() + 1)).slice(-2);
    const startDay = ('0' + yesterday.getDate()).slice(-2);
    const startHour = ('0' + yesterday.getHours()).slice(-2);

    this.datetimeRange.start = `${startYear}-${startMonth}-${startDay}T${startHour}:00`;
    this.datetimeRange.end = `${year}-${month}-${day}T${hour}:00`;
  }

  updateValue() {
    const start = new Date(this.datetimeRange.start);
    const end = new Date(this.datetimeRange.end);
    
    const startUTC = this.formatDatetime(start);
    const endUTC = this.formatDatetime(end);
    
    this.dateTimeSelected.emit({ start: startUTC, end: endUTC });
  }

  private formatDatetime(date: Date): string {
    const year = date.getUTCFullYear();
    const month = ('0' + (date.getUTCMonth() + 1)).slice(-2);
    const day = ('0' + date.getUTCDate()).slice(-2);
    const hour = ('0' + date.getUTCHours()).slice(-2);
    return `${year}-${month}-${day} ${hour}:00:00`;
  }

  // ControlValueAccessor implementation
  onChange: any = () => {};
  onTouch: any = () => {};

  writeValue(obj: any): void {
    this.datetimeRange = obj || { start: '', end: '' };
  }

  registerOnChange(fn: any): void {
    this.onChange = fn;
  }

  registerOnTouched(fn: any): void {
    this.onTouch = fn;
  }
}
