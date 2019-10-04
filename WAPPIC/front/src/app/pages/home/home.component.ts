import { Component, OnInit } from '@angular/core';
import { MenuappService } from 'src/app/services/menuapp.service';
import { IMenuapp } from '../../../../../cross/models/menuapp';
import { menuapp } from '../../../../../cross/mocks/data';
import { Entity, Set } from '@diaspora/diaspora';
import { BehaviorSubject } from 'rxjs';

@Component({
	selector: 'app-home',
	templateUrl: './home.component.html',
	styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

	public menuApp = menuapp;

	constructor( private menuappService: MenuappService ) {	}

	ngOnInit() {}

	goToUrl( url: string ) {
		if ( url.match(/^((?!http|\/).)*$/gm )) {
			console.log(url);
		} else {
			document.location.href = url;
		}
	}
}
