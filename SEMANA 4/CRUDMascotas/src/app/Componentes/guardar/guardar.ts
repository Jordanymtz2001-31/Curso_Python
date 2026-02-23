import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Servidor } from '../../Servidor/servidor';
import { Router } from '@angular/router';
import { Mascota } from '../../Entidad/Mascota';
import { HttpResponse } from '@angular/common/http';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-guardar',
  imports: [FormsModule],
  templateUrl: './guardar.html',
  styleUrl: './guardar.css',
})
export class Guardar implements OnInit {

  //Inyectamos El Servidor y el Router en el constructor
  constructor(private servidor: Servidor, private router: Router) {}

  mascota : Mascota = new Mascota()
  mascotas !: Mascota[]

  ngOnInit(): void {}

  guardar(){
    this.servidor.guardar(this.mascota).subscribe({
      next: (response: HttpResponse<Mascota>) => {
        if (response.status == 201) {
          Swal.fire({
            title: 'Mascota Guardada',
            text : 'La mascota ha sido guardada con exito',
            icon : 'success',
            showConfirmButton: false,
            timer: 1500
          });
          this.router.navigate(['listar']);
        }
      },
      error: (error) => {
        if (error.status == 400) {
          Swal.fire({
            title: 'Error al guardar la mascota',
            text : 'Los campos no pueden estar vacios',
            icon : 'error',
            showConfirmButton: false,
            timer: 1500
          });
        }
      },
      complete: () => {
        console.log("El observable se ha completado");
      }
    })
  }

  cancelar(){
    Swal.fire({
      title: 'Cancelar',
      text: "Se ha cancelado la acción",
      icon: 'error',
    })
      this.router.navigate(['listar']);
  }
}
