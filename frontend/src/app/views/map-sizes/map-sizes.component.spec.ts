import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MapSizesComponent } from './map-sizes.component';

describe('MapSizesComponent', () => {
  let component: MapSizesComponent;
  let fixture: ComponentFixture<MapSizesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MapSizesComponent]
    });
    fixture = TestBed.createComponent(MapSizesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
