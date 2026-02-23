import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Servidor } from '../../Servidor/servidor';
import { Router } from '@angular/router';
import { Mascota } from '../../Entidad/Mascota';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-editar',
  imports: [FormsModule],
  templateUrl: './editar.html',
  styleUrl: './editar.css',
})
export class Editar implements OnInit {

  //Inyectamos el Servidor y el Router en el constructor
  constructor(private servidor: Servidor, private router: Router) {}

  mascota : Mascota = new Mascota()


  ngOnInit(): void {

    this.buscar();
  }

  buscar(){
    let id = Number(localStorage.getItem('id'));

    this.servidor.buscar(id).subscribe((data) => {
      this.mascota = data;
    });
  }

  editar(){
    this.servidor.editar(this.mascota).subscribe(() => {
      Swal.fire({
        icon: 'success',
        title: 'Mascota Editada',
        showConfirmButton: false,
        timer: 1500
      });
      this.router.navigate(['listar']);
    }, (error) => {
      if (error.status == 400) {
        Swal.fire({
          title: 'Error al editar la mascota',
          text : 'Los campos no pueden estar vacios',
          icon : 'error',
          showConfirmButton: false,
          timer: 1500
        });
      }
    }
  )
  }

  cancelar(){
    this.router.navigate(['listar']);
  }
}
