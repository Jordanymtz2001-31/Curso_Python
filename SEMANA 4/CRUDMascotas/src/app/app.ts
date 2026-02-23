import { Component, signal } from '@angular/core';
import { Router, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('CRUDMascotas');

  //Inyectamos el router
  constructor(private router: Router) {}

  //Metodo para navegar al metodo de listar
  listar() {
    this.router.navigate(['listar']);
  }

  //Metodo para navegar al metodo de guardar
  guardar() {
    this.router.navigate(['guardar']);
  }
}
