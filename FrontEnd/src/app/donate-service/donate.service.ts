import { Injectable, numberAttribute } from '@angular/core';

@Injectable({
    providedIn: 'root'
})
export class DonateService {
    _school: string | null;
    _meals: any[];
    _snack: any[];
    constructor() {
        this._school = null;
        this._meals = []
        this._snack = [];
    }
    set school(school: string) {
        this._school = school;
    }
    addMeal(meal: object) {
        this._meals.push(meal);
    }
    addSnack(snack: object) {
        this._snack.push(snack);
    }
    removeMeal(index: number) {
        this._meals.splice(index);
    }
    removeSnack(index: number) {
        this._snack.splice(index);
    }
    
}
