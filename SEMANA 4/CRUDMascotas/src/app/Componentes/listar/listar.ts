import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Servidor } from '../../Servidor/servidor';
import { Router } from '@angular/router';
import { Mascota } from '../../Entidad/Mascota';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-listar',
  imports: [FormsModule],
  templateUrl: './listar.html',
  styleUrl: './listar.css',
})
export class Listar implements OnInit{

  //Inyectamos el Servidor en el constructor
  constructor(private servidor: Servidor, private router: Router) {}

  mascota : Mascota = new Mascota();
  mascotas !: Mascota[]

  ngOnInit() : void{
    this.listar();
  }

  listar(){
    this.servidor.listar().subscribe({
      //Next se ejecuta cada que el observable emite valores
      next: (data) => {
        this.mascotas = data;
      },

      //El error se ejecuta cuando el observable emite un error del Backend
      error: (error) => {
        console.log("Error por parte del Backend al obtener los datos: ", error);
      },

      //El complete se ejecuta cuando el observable se completa
      complete: () => {
        console.log("El observable se ha completado");
      }
    })
  }

  editar(mascota: Mascota){
    Swal.fire({
      title: 'Cargar mascota',
      text: "No podra revertir los cambios",
      icon: 'success',
      showDenyButton: true,
      showCancelButton: false,
      cancelButtonColor : '#d33'
    }).then(() => {
      localStorage.setItem('id', mascota.id.toString());
      this.router.navigate(['editar']);
    })
  }
  

  eliminar(mascota: Mascota){
    Swal.fire({
      title: '¿Desea eliminar la mascota?',
      text: "No podra revertir los cambios",
      icon: 'warning',
      showDenyButton: true,
      showCancelButton: false,
      cancelButtonColor : '#d33',
      confirmButtonText: 'Si',
      confirmButtonColor: '#3085d6'
    }).then((result) => {
      if(result.isConfirmed){
        this.servidor.eliminar(mascota.id).subscribe(() => {
          Swal.fire({
            icon: 'success',
            title: 'Mascota Eliminada',
            showConfirmButton: false,
            timer: 1500
          })
          this.listar()
        })
      }
    })
  }

}
