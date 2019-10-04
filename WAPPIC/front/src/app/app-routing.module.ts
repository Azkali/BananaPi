import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';

import { SettingsComponent } from 'src/app/pages/settings/settings.component';
import { HomeComponent } from './pages/home/home.component';
import { menuapp } from '../../../cross/mocks/data';

const appRoutes: Routes = [
	{ path: '', redirectTo: '/home', pathMatch: 'full' },
	{ path: 'settings', component: SettingsComponent },
	{ path: 'home', component: HomeComponent },
];


@NgModule({
	declarations: [],
	imports: [
		RouterModule.forRoot(
			appRoutes,
		)],
	exports: [
		RouterModule,
	],
})
export class AppRoutingModule { }
