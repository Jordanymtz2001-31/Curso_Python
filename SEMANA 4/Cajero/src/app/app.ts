import { Component, signal } from '@angular/core';
import { Router, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('Cajero');

  //Creamos un constructor para inyectar el router
  constructor(private router: Router) {}

  //Metodo para navegar hacia las transacciones
  transacciones() {
    this.router.navigate(['transacciones']);
  }

  //Metodo para navegar hacia el dashboard
  dashboard() {
    this.router.navigate(['dashboard']);
  }

  //Metodo para navegar hacia la inicializacion
  inicializacion() {
    this.router.navigate(['inicializacion']);
  }

}
