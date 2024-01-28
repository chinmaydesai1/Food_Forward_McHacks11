import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {
    NbThemeModule,
    NbInputModule,
    NbCardModule,
    NbLayoutModule,
    NbSidebarService,
    NbSidebarModule,
    NbMenuModule,
    NbMenuService,
    NbIconModule,

} from '@nebular/theme'
import { FormDataService } from './form-data/form-data.service';
import { BusinessOrStudentService } from './business-or-student/business-or-student.service';
import { DonateService } from './donate-service/donate.service';
import { RouterModule } from '@angular/router'
import { HttpClientModule } from '@angular/common/http'
import { NbEvaIconsModule } from '@nebular/eva-icons'
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MealSnackInputComponent } from './meal-snack-input/meal-snack-input.component';
@NgModule({
    declarations: [
        AppComponent
    ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        BrowserModule,
        AppRoutingModule,
        NbThemeModule.forRoot({ name: 'dark' }),
        NbInputModule,
        NbCardModule,
        NbLayoutModule,
        NbEvaIconsModule,
        NbSidebarModule,
        NbMenuModule.forRoot(),
        NbIconModule,
        HttpClientModule,
        RouterModule.forRoot([
            { path: 'donate', component: MealSnackInputComponent }
        ])
    ],
    providers: [NbSidebarService, NbMenuService, FormDataService, BusinessOrStudentService, DonateService],
    bootstrap: [AppComponent]
})
export class AppModule { }
