import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Servidor } from '../../Servidor/servidor';
import { Perfil } from '../../Entidad/perfil';

@Component({
  selector: 'app-listar',
  imports: [FormsModule],
  templateUrl: './listar.html',
  styleUrl: './listar.css',
})
export class Listar implements OnInit {
  //Inyectamos el servidor
  constructor(private service: Servidor) {}

  // Creamos un arreglo de tipo Perfil
  perfiles!: Perfil[];

  // El metodo ngOnInit ejecuta instrucciones automaticamente una vez que el componente carga.
  ngOnInit(): void {
    this.listar();
  }
  // Funcion listar
  listar() {
    // LLmamos mediante la inyeccion del service al metodo listarPerfil
    this.service.listarPerfil().subscribe((data) => {
      // Almacenamos el cuerpo de la repsuesta http en la variable perfiles
      this.perfiles = data;
    });
  }
}
