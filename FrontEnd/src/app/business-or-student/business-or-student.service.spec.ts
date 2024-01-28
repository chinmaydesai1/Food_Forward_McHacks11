import { TestBed } from '@angular/core/testing';

import { BusinessOrStudentService } from './business-or-student.service';

describe('BusinessOrDataService', () => {
    let service: BusinessOrStudentService;

    beforeEach(() => {
        TestBed.configureTestingModule({});
        service = TestBed.inject(BusinessOrStudentService);
    });

    it('should be created', () => {
        expect(service).toBeTruthy();
    });
});
