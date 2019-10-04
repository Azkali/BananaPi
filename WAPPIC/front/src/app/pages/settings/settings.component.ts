import { Component, OnInit } from '@angular/core';
import { serviceapp } from '../../../../../cross/mocks/data';

@Component({
	selector: 'app-settings',
	templateUrl: './settings.component.html',
	styleUrls: ['./settings.component.scss']
})
export class SettingsComponent implements OnInit {

	public serviceApp = serviceapp;
	public selectedIdx = 0;

	constructor() { }

	ngOnInit() { }

	public triggerStatusChange(item, index: number) {
		const raspicls = document.getElementsByClassName('raspi-service') as HTMLCollectionOf<HTMLElement>;
		this.selectedIdx = index;


		this.serviceApp.forEach((service) => {
			// service.statusStr = 'Enable or Disable';
			if ( item.status === false ) {
				item.statusStr = 'Enable';
				raspicls[index].style.backgroundColor = 'lightgreen';
			} else if (item.status === true) {
				item.statusStr = 'Disable';
				raspicls[index].style.backgroundColor = '#DC143C';
			}
		});

	}
}

