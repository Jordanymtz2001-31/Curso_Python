import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Servidor } from '../../Servidor/servidor';
import { Computadora } from '../../Entidad/computadora';

@Component({
  selector: 'app-listar',
  imports: [FormsModule],
  templateUrl: './listar.html',
  styleUrl: './listar.css',
})
export class Listar implements OnInit {

  //Inyectamos al servidor
  constructor(private servidor: Servidor) {}

  //Hacemos una variable para almacenar las computadoras
  computadoras !: Computadora[];

  ngOnInit(): void {
    this.listar();
  }

  //Metodos para listar
  listar() {
    this.servidor.listar().subscribe((data) => { //Para obtener los datos y manupularlo necesitamos el subscribe y en el data alamcenamos los datos del servidor (backend)
      this.computadoras = data  //Le asignamos los datos de data a la variable computadoras
    })
  }

}
