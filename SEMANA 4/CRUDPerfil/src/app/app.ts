import { Component, signal } from '@angular/core';
import { Router, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css',
})
export class App {
  protected readonly title = signal('CRUDPerfiles');

  // Inyectamos el router por medio de un constructor
  constructor(private router: Router) {}

  // Creamos los metodos de los eventos click
  listar() {
    this.router.navigate(['listar']);
  }

  nuevo() {
    this.router.navigate(['guardar']);
  }
}
