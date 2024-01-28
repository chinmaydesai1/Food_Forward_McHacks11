import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, NgForm, NgModel, ReactiveFormsModule, FormGroup, FormControl, Validators } from '@angular/forms';
import { NbInputModule, NbCardModule, NbButtonModule, NbAlertModule, NbFormFieldModule, NbIconModule } from '@nebular/theme';
@Component({
    selector: 'app-sign-up',
    standalone: true,
    imports: [NbInputModule, NbCardModule, FormsModule, NbButtonModule, NbAlertModule, CommonModule, NbFormFieldModule, NbIconModule, ReactiveFormsModule],
    templateUrl: './Sign-Up.component.html',
    styleUrls: ['./Sign-Up.component.scss']
})
export class SignUpComponent {

}
