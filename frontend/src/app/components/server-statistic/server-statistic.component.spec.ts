import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ServerStatisticComponent } from './server-statistic.component';

describe('ServerStatisticComponent', () => {
  let component: ServerStatisticComponent;
  let fixture: ComponentFixture<ServerStatisticComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ServerStatisticComponent]
    });
    fixture = TestBed.createComponent(ServerStatisticComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
