import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../Servidor/api-service';

@Component({
  selector: 'app-noticias',
  imports: [],
  templateUrl: './noticias.html',
  styleUrl: './noticias.css',
})
export class Noticias implements OnInit {

  constructor(private apiService: ApiService) { }

  noticias = '';

  ngOnInit(): void {
    
    this.apiService.getNoticias().subscribe((data) => { //Obtenemos el mensaje de bienvenida del servidor
      this.noticias = data.noticias; //Lo asignamos a la variable
    });
  }

}
