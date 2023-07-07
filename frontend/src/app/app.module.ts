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

// Components
import { StatisticComponent } from './components/statistic/statistic.component';
import { LiveGraphComponent } from './components/live-graph/live-graph.component';

// Views
import { HomeComponent } from './views/home/home.component';
import { MapsComponent } from './views/maps/maps.component';
import { RegionsComponent } from './views/regions/regions.component';
import { MapSizesComponent } from './views/map-sizes/map-sizes.component';
import { GameModesComponent } from './views/game-modes/game-modes.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    MapsComponent,
    RegionsComponent,
    MapSizesComponent,
    GameModesComponent,
    StatisticComponent,
    LiveGraphComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    MatCardModule,
    MatToolbarModule,
    MatButtonModule,
    FlexLayoutModule,
    MatGridListModule,
    BrowserAnimationsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
