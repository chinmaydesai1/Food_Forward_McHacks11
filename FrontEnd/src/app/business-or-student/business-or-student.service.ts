import { Injectable } from '@angular/core';
import { Subject } from 'rxjs'
@Injectable({
    providedIn: 'root'
})
export class BusinessOrStudentService {
    _businessOrData: boolean;
    businessOrDataSubject: Subject<any> = new Subject<any>();
    constructor() {
        this._businessOrData = false;
    }
    set businessOrData(busOrStudent: boolean) {
        this._businessOrData = busOrStudent;
        this.businessOrDataSubject.next(this._businessOrData);
    }
    get businessOrData() {
        return this._businessOrData;
    }
}
