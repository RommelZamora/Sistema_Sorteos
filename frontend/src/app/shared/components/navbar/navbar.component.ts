import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {

  constructor(private router: Router) {}

  menuOpen = false;

  toggleMenu() {
    this.menuOpen = !this.menuOpen;
  }
  navigateToHome() {
    this.router.navigate(['/home']);
  }

  navigateToLogin() {
    this.router.navigate(['/login']);
  }
}
