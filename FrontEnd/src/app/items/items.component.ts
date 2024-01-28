import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NbInputModule, NbCardModule, NbButtonModule, NbAlertModule, NbFormFieldModule, NbIconModule, NbOptionModule, NbSelectModule } from '@nebular/theme';
import { HttpClient } from '@angular/common/http';
@Component({
    selector: 'app-items',
    standalone: true,
    imports: [CommonModule, NbInputModule, NbCardModule, NbButtonModule, NbAlertModule, NbFormFieldModule, NbIconModule, NbOptionModule, NbSelectModule],
    templateUrl: './items.component.html',
    styleUrls: ['./items.component.scss']
})
export class ItemsComponent {
    itemsList: any;
    universityName: any;
    constructor(private http: HttpClient) {
    }
    async displayItems(universityName: string) {
        this.universityName = universityName;
        const response = await this.http.post("http://127.0.0.1:5000/donateData", { university: universityName }).toPromise();
        console.log(response);
    }
}
