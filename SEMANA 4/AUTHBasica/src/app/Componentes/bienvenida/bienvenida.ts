import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../Servidor/api-service';

@Component({
  selector: 'app-bienvenida',
  imports: [],
  templateUrl: './bienvenida.html',
  styleUrl: './bienvenida.css',
})
export class Bienvenida implements OnInit {

  mensage = '';

  //Inyectamos el servicio
  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.apiService.getBienvenida().subscribe((data) => {
      this.mensage = data.Mensaje;
    }); //Obtenemos el mensaje de bienvenida del servidor y se lo asignamos a la variable
  }

}
