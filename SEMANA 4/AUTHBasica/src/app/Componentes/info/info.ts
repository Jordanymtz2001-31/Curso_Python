import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../Servidor/api-service';

@Component({
  selector: 'app-info',
  imports: [],
  templateUrl: './info.html',
  styleUrl: './info.css',
})
export class Info implements OnInit {

  constructor(private apiService: ApiService) { }

  informacion = ''
  ngOnInit(): void {

    this.apiService.getInfo().subscribe((data) => { //Obtenemos el mensaje de bienvenida del servidor
      this.informacion = data.info; //Lo asignamos a la variable
    });
  }

}
