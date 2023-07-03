import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';

// Components
import { ServerStatsComponent } from './components/server-stats/server-stats.component';

// Views
import { HomeComponent } from './views/home/home.component';


@NgModule({
  declarations: [
    AppComponent,
    ServerStatsComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
