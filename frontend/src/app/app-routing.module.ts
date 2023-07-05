import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './views/home/home.component';
import { GameModesComponent } from './views/game-modes/game-modes.component';
import { MapSizesComponent } from './views/map-sizes/map-sizes.component';
import { MapsComponent } from './views/maps/maps.component';
import { RegionsComponent } from './views/regions/regions.component';

const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'game-modes', component: GameModesComponent },
  { path: 'map-sizes', component: MapSizesComponent },
  { path: 'maps', component: MapsComponent },
  { path: 'regions', component: RegionsComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
