import { Component } from '@angular/core';

@Component({
  selector: 'app-sorteos',
  templateUrl: './sorteos.component.html',
  styleUrls: ['./sorteos.component.css']
})
export class SorteosComponent {
  onInput(event: Event): void {
    const inputElement = event.target as HTMLInputElement;
    if (inputElement.value) {
      inputElement.classList.add('has-content');
    } else {
      inputElement.classList.remove('has-content');
    }
  }
  participants: { name: string, checked: boolean }[] = [
    { name: 'Ana Lucia', checked: false },
    { name: 'Carlos Andres', checked: false },
    // { name: 'Maria Fernada', checked: false },
    // { name: 'Jose Miguel', checked: false }
  ];
  newParticipant: string = '';

  addParticipant() {
    if (this.newParticipant.trim()) {
      this.participants.push({ name: this.newParticipant.trim(), checked: false });
      this.newParticipant = '';
    }
  }

  toggleCheck(index: number) {
    this.participants[index].checked = !this.participants[index].checked;
  }

  removeParticipant(index: number) {
    this.participants.splice(index, 1);
  }

  publications: { name: string }[] = [
    { name: 'Imagen.001'},
    { name: 'Imagen.002' },
    { name: 'Imagen.003'},
    { name: 'Imagen.004' }
  ];

  toggleUp() {
    // Algun metodo que quieran usar
  }

  removePublication(index: number) {
    this.publications.splice(index, 1);
  }
}