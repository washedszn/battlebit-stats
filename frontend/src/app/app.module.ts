import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { MatCardModule } from '@angular/material/card';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { FlexLayoutModule } from '@angular/flex-layout';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatDividerModule } from '@angular/material/divider';
import { MatIconModule } from '@angular/material/icon';
import { MatMenuModule } from '@angular/material/menu';
import { MatTooltipModule } from '@angular/material/tooltip';
import { MatChipsModule } from '@angular/material/chips';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatNativeDateModule } from '@angular/material/core';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';

// Components
import { StatisticComponent } from './components/statistic/statistic.component';
import { LiveGraphComponent } from './components/live-graph/live-graph.component';

// Views
import { ServersComponent } from './views/servers/servers.component';
import { MapsComponent } from './views/maps/maps.component';
import { RegionsComponent } from './views/regions/regions.component';
import { MapSizesComponent } from './views/map-sizes/map-sizes.component';
import { GameModesComponent } from './views/game-modes/game-modes.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ServerStatisticComponent } from './components/server-statistic/server-statistic.component';
import { FloatingBarChartComponent } from './components/floating-bar-chart/floating-bar-chart.component';
import { DatetimeRangePickerComponent } from './components/datetime-range-picker/datetime-range-picker.component';
import { NoDataComponent } from './components/no-data/no-data.component';

@NgModule({
  declarations: [
    AppComponent,
    ServersComponent,
    MapsComponent,
    RegionsComponent,
    MapSizesComponent,
    GameModesComponent,
    StatisticComponent,
    LiveGraphComponent,
    ServerStatisticComponent,
    FloatingBarChartComponent,
    DatetimeRangePickerComponent,
    NoDataComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    MatCardModule,
    MatToolbarModule,
    MatButtonModule,
    FlexLayoutModule,
    MatDividerModule,
    MatMenuModule,
    MatTooltipModule,
    MatIconModule,
    MatChipsModule,
    MatFormFieldModule,
    ReactiveFormsModule,
    FormsModule,
    MatInputModule,
    MatGridListModule,
    BrowserAnimationsModule,
    MatNativeDateModule,
    MatDatepickerModule,
    MatProgressSpinnerModule
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
