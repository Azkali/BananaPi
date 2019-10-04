import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';

@Component({
	selector: 'app-goback',
	templateUrl: './goback.component.html',
	styleUrls: ['./goback.component.scss']
})
export class GobackComponent implements OnInit {

	constructor(private _location: Location) { }

	ngOnInit() {
	}

	public backClicked() {
		this._location.back();
	}

}
