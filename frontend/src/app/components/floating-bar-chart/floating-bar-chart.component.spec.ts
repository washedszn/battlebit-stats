import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FloatingBarChartComponent } from './floating-bar-chart.component';

describe('FloatingBarChartComponent', () => {
  let component: FloatingBarChartComponent;
  let fixture: ComponentFixture<FloatingBarChartComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [FloatingBarChartComponent]
    });
    fixture = TestBed.createComponent(FloatingBarChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
