import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule, FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';
import { NbInputModule, NbCardModule, NbButtonModule, NbAlertModule, NbFormFieldModule, NbIconModule } from '@nebular/theme';
import { BusinessOrStudentService } from '../business-or-student/business-or-student.service';
import { FormDataService } from '../form-data/form-data.service';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
@Component({
    selector: 'app-log-in',
    standalone: true,
    imports: [CommonModule, NbInputModule, NbCardModule, NbButtonModule, NbAlertModule, NbFormFieldModule, NbIconModule, FormsModule, ReactiveFormsModule],
    templateUrl: './log-in.component.html',
    styleUrls: ['./log-in.component.scss']
})
export class LogInComponent {
    LogInForm: any;
    studOrbus: string | null;
    show = false;
    constructor(private http: HttpClient, private fb: FormBuilder, private busOrStud: BusinessOrStudentService, private router: Router) {
        this.LogInForm = fb.group({
            email: ['', Validators.required, Validators.pattern("[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]+")],
            password: ['', Validators.required, Validators.minLength(8)]
        })
        this.studOrbus = null;
    }
    onLogInFormSubmit(formType: string) {
        let formData = new FormData();
        formData.append("email", this.LogInForm.controls.email.value);
        formData.append("password", this.LogInForm.controls.password.value);
        if (formType == "student") {
            const response = this.http.post("http://127.0.0.1:5000/studentFormData/logIn", formData, { responseType: 'json' });
            console.log(response);
            this.busOrStud.businessOrData = true;
            this.busOrStud.signedIn = true;
            this.router.navigate(["/checkItems"]);
        }
        else {
            const response = this.http.post("http://127.0.0.1:5000/businessFormData/logIn", formData, { responseType: 'json' });
            console.log(response);
            this.busOrStud.businessOrData = false;
            this.busOrStud.signedIn = true;
            this.router.navigate(["/donate"]);
        }
    }
}
