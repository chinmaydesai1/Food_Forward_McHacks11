import { Component } from '@angular/core';
import { NbSidebarService, NbMenuItem, NbMenuService } from '@nebular/theme'
@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.scss']
})
export class AppComponent {
    title = 'FrontEnd';
    items: NbMenuItem[] = [
        {
            title: 'Home',
            icon: 'home-outline',
            link: '/',
        },
        {
            title: 'Check Items',
            icon: 'browser-outline',
            link: 'checkItems',
        },
        {
            title: 'Donate',
            icon: 'corner-down-left-outline',
            link: 'donate',
            hidden: false,

        },
    ]
    constructor(private sidebarService: NbSidebarService, private menuService: NbMenuService) { }
    toggle() {
        this.sidebarService.toggle(true)
        return false
    }
    menuToggle() {
        this.menuService.onItemClick()
    }
}
