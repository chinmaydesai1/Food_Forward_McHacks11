import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule, FormBuilder, Validators } from '@angular/forms';
import { NbInputModule, NbCardModule, NbButtonModule, NbAlertModule, NbFormFieldModule, NbIconModule, NbOptionModule, NbSelectModule } from '@nebular/theme';
import { BusinessOrStudentService } from '../business-or-student/business-or-student.service';
import { FormDataService } from '../form-data/form-data.service';
import { Router } from '@angular/router';
@Component({
    selector: 'app-sign-up',
    standalone: true,
    imports: [NbInputModule, NbCardModule, FormsModule, NbButtonModule, NbAlertModule, CommonModule, NbFormFieldModule, NbIconModule, ReactiveFormsModule, NbOptionModule, NbSelectModule],
    templateUrl: './Sign-Up.component.html',
    styleUrls: ['./Sign-Up.component.scss']
})
export class SignUpComponent {
    studentForm: any;
    businessForm: any;
    showStudentForm = false;
    showBusinessForm = false;
    show = false;
    constructor(private fb: FormBuilder, private busOrStud: BusinessOrStudentService, private formData: FormDataService, private router: Router) {
        this.studentForm = this.fb.group({
            userName: ['', [Validators.required, Validators.minLength(5)]],
            email: ['', [Validators.required, Validators.pattern("[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]+")]],
            school: ['', [Validators.required]],
            password: ['', [Validators.required, Validators.minLength(8)]]
        });
        this.businessForm = this.fb.group({
            businessName: ['', [Validators.required, Validators.minLength(4)]],
            address: ['', [Validators.required]],
            contactNumber: ['', [Validators.required]],
            password: ["", [Validators.required, Validators.minLength(8)]]
        })
    }
    onFormSelect(selection: string) {
        if (selection == "student")
            this.showStudentForm = true;
        else
            this.showBusinessForm = true;
    }

    onStudentFormSubmit() {
        console.log(this.studentForm.value);
        this.busOrStud.signedIn = true;
        this.busOrStud.businessOrData = true;
        this.formData.studentFormData = this.studentForm.value;
        let response = this.formData.postStudentFormData();
        console.log(response);
        this.router.navigate(['/items']);
    }
    onBusinessFormSubmit() {
        console.log(this.businessForm.value);
        this.busOrStud.signedIn = true;
        this.busOrStud.businessOrData = false;
        this.formData.businessFormData = this.businessForm.value;
        let response = this.formData.postBusinessData();
        console.log(response);
        this.router.navigate(['/donate']);
    }
    studentFormPicked() {
        this.showStudentForm = true;
        this.show = true;
    }
    businessFormPicked() {
        this.showBusinessForm = true;
        this.show = true;
    }
}