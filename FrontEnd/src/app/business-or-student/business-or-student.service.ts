import { Injectable } from '@angular/core';
import { Subject } from 'rxjs'
@Injectable({
    providedIn: 'root'
})
export class BusinessOrStudentService {
    _businessOrData: boolean;
    businessOrDataSubject: Subject<any> = new Subject<any>();
    _signedIn: boolean;
    constructor() {
        this._businessOrData = false;
        this._signedIn = false;
    }
    set businessOrData(busOrStudent: boolean) {
        this._businessOrData = busOrStudent;
        this.businessOrDataSubject.next({ busOrStud: this._businessOrData });
    }
    set signedIn(signIn: boolean) {
        this._signedIn = signIn;
        this.businessOrDataSubject.next({ signedIn: this._signedIn });
    }
    get businessOrData() {
        return this._businessOrData;
    }
    get signedIn() {
        return this._signedIn;
    }
}
