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
    NbButtonModule

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
import { SignUpComponent } from './sign-up/Sign-Up.component';
import { LogInComponent } from './log-in/log-in.component';
<<<<<<< HEAD
import { ItemsComponent } from './items/items.component';
=======
import { HomeComponent } from './home/home.component';
>>>>>>> 08a8a1c146a7ad9cdf73815aa5699166045d6099
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
        NbButtonModule,
        HttpClientModule,
        LogInComponent,
        RouterModule.forRoot([
            { path: 'donate', component: MealSnackInputComponent },
            { path: 'signUp', component: SignUpComponent },
            { path: 'logIn', component: LogInComponent },
<<<<<<< HEAD
            { path: "items", component: ItemsComponent }
=======
            { path: '', component: HomeComponent }
            //{ path: "checkItems" }
>>>>>>> 08a8a1c146a7ad9cdf73815aa5699166045d6099
        ])
    ],
    providers: [NbSidebarService, NbMenuService, FormDataService, BusinessOrStudentService, DonateService],
    bootstrap: [AppComponent]
})
export class AppModule { }
