import { Injectable } from '@angular/core';

import { Diaspora, Model, Adapter, Set, EntityUid } from '@diaspora/diaspora';
import DataAccessLayer = Adapter.DataAccessLayer;
import { from, BehaviorSubject, AsyncSubject, forkJoin } from 'rxjs';
import * as _ from 'lodash';




@Injectable({
	providedIn: 'root'
})
export class MenuappService {

	constructor() {
		Diaspora.createNamedDataSource( 'main', 'inMemory' );
	}
}
