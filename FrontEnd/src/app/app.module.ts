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
import { RouterModule } from '@angular/router'
import { HttpClientModule } from '@angular/common/http'
import { NbEvaIconsModule } from '@nebular/eva-icons'
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

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
    ],
    providers: [NbSidebarService, NbMenuService],
    bootstrap: [AppComponent]
})
export class AppModule { }
