import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import {
    FormsModule,
    ReactiveFormsModule,
    Validators,
    FormBuilder,
    FormArray
} from '@angular/forms'
import {
    NbInputModule,
    NbCardModule,
    NbButtonModule,
    NbAlertModule,
    NbFormFieldModule,
    NbIconModule,
    NbListModule,
    NbSpinnerModule,
    NbSelectModule
} from '@nebular/theme'
@Component({
    selector: 'app-meal-snack-input',
    standalone: true,
    imports: [CommonModule,
        NbInputModule,
        NbCardModule,
        NbButtonModule,
        NbAlertModule,
        NbFormFieldModule,
        NbIconModule,
        NbListModule,
        NbSpinnerModule,
        FormsModule,
        NbSelectModule,
        ReactiveFormsModule
    ],
    templateUrl: './meal-snack-input.component.html',
    styleUrls: ['./meal-snack-input.component.scss']
})
export class MealSnackInputComponent {
    form = this.fb.group({
        university: ['', Validators.required],
        meals: this.fb.array([]),
        snacks: this.fb.array([])
    })
    disableMinusForMeals: boolean = true;
    disableMinusForSnacks: boolean = true;
    atleastOneFieldIsMandatory: boolean = true;
    constructor(private fb: FormBuilder, private http: HttpClient) {
        this.meals.push(this.fb.group({
            mealName: [''],
            mealNum: ['']
        }))
        this.snacks.push(this.fb.group({
            snackName: [''],
            snackNum: ['']
        }))
    }
    get meals() {
        return this.form.controls['meals'] as FormArray;
    }
    get snacks() {
        return this.form.controls['snacks'] as FormArray;
    }
    addMeal() {
        if (this.meals.length == 1) {
            this.meals.at(0).setValidators(Validators.required);
        }
        this.meals.push(this.fb.group({
            mealName: ['', Validators.required],
            mealNum: ['', Validators.required]
        }))
        this.disableMinusForMeals = false;
    }
    addSnack() {
        if (this.snacks.length == 1) {
            this.snacks.at(0).setValidators(Validators.required);
        }
        this.snacks.push(this.fb.group({
            snackName: ['', Validators.required],
            snackNum: ['', Validators.required]
        }))
        this.disableMinusForSnacks = false;
    }
    removeMeal(index: number) {
        if (this.meals.length > 2)
            this.meals.removeAt(index);
        else if (this.meals.length == 2) {
            this.meals.removeAt(index);
            this.disableMinusForMeals = true;
            this.meals.at(0).removeValidators(Validators.required);
        }
    }
    removeSnack(index: number) {
        if (this.snacks.length > 2)
            this.snacks.removeAt(index);
        else if (this.meals.length == 2) {
            this.snacks.removeAt(index);
            this.disableMinusForSnacks = true;
            this.snacks.at(0).removeValidators(Validators.required);
        }
    }
    async onSubmit() {
        if (this.meals.length == 1 && this.snacks.length == 1) {
            let meal = this.meals.at(0).value;
            let snack = this.snacks.at(0).value;
            if (meal.mealName == '' && meal.mealNum == '' && snack.snackName == '' && snack.snackNum == '') {
                this.atleastOneFieldIsMandatory = false;
                console.log("bullshit")
                return;
            }
        }
        await this.sendData();
    }
    async sendData() {
        const formData = new FormData();
        formData.append('university', JSON.stringify(this.form.controls.university.value));
        const mealsArray = [];
        for (let i = 0; i < this.meals.length; i++) {
            mealsArray.push(this.meals.at(i).value);
        }
        const snacksArray = []
        for (let i = 0; i < this.snacks.length; i++) {
            snacksArray.push(this.snacks.at(i).value);
        }
        formData.append('meals', JSON.stringify(mealsArray));
        formData.append('snacks', JSON.stringify(snacksArray));
        console.log(this.form.controls.university.value);
        console.log(JSON.stringify(mealsArray));
        console.log(JSON.stringify(snacksArray));
        console.log(await this.http.post("http://127.0.0.1:5000/donateData", formData, { responseType: 'json' }).toPromise())
    }
}
