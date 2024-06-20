import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  createRaffle() {
    console.log('Crear Sorteo button clicked!');
    // Add navigation or other logic here
  }
}
