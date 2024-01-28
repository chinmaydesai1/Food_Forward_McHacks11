import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
    providedIn: 'root'
})
export class FormDataService {
    _studentFormData: object | null;
    _businessFormData: object | null;
    constructor(private http: HttpClient) {
        this._studentFormData = null;
        this._businessFormData = null;
    }
    set studentFormData(studentData: object) {
        this._studentFormData = studentData;
    }
    async postStudentFormData() {
        return await this.http.post("http://127.0.0.1:5000/studentFormData", this._studentFormData, { responseType: 'json' }).toPromise();
    }
    set businessFormData(businessData: object) {
        this._businessFormData = businessData
    }
    async postBusinessData() {
        return await this.http.post("http://127.0.0.1:5000/businessData", this._businessFormData, { responseType: "json" }).toPromise();
    }
}
