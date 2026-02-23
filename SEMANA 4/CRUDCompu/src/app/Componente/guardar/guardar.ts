import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { form } from '@angular/forms/signals';
import { Servidor } from '../../Servidor/servidor';
import { Computadora } from '../../Entidad/computadora';
import { Router } from '@angular/router';

@Component({
  selector: 'app-guardar',
  imports: [FormsModule],
  templateUrl: './guardar.html',
  styleUrl: './guardar.css',
})
export class Guardar implements OnInit {

  //Creamos el constructor para inyectar el servicio y el router
  constructor(private servidor: Servidor, private router: Router) { }

  //Intancia par crear una computadora
  computadora: Computadora = new Computadora();

  ngOnInit(): void {
    
  }

  //Creamos el metodo para guardar
  guardar() {
    this.servidor.guardar(this.computadora).subscribe((data) => {
      this.router.navigate(['listar']);
    });
  }

  cancelar() {
    this.router.navigate(['listar']);
  }

}
