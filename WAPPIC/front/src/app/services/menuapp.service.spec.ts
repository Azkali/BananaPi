import { TestBed } from '@angular/core/testing';

import { MenuappService } from './menuapp.service';

describe('MenuappService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: MenuappService = TestBed.get(MenuappService);
    expect(service).toBeTruthy();
  });
});
