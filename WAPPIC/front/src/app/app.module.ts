import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { AppRoutingModule } from './app-routing.module';
import { SettingsComponent } from './pages/settings/settings.component';
import { HomeComponent } from './pages/home/home.component';
import { GobackComponent } from './components/goback/goback.component';
import { ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';

@NgModule({
	declarations: [
		AppComponent,
		SettingsComponent,
		HomeComponent,
		GobackComponent,
	],
	imports: [
		BrowserModule,
		MatGridListModule,
		MatCardModule,
		MatIconModule,
		AppRoutingModule,
	],
	providers: [],
	bootstrap: [AppComponent]
})
export class AppModule { }
