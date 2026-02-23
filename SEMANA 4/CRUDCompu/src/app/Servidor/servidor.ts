import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Computadora } from '../Entidad/computadora';

@Injectable({
  providedIn: 'root',
})
export class Servidor {

  //Inyectanos al cliente HTTP
  constructor(private http: HttpClient) {}

  //Ruta de acceso al servidor en el backend
  url = 'http://localhost:8000/compu/';

  //Metodo para listar
  listar() { //No recibimos nada como parametro
    return this.http.get<Computadora[]>(this.url + 'listar/');
  }

  //Metodo para guardar
  guardar(compu: Computadora) { //Recibimos un objeto de tipo Computadora
    return this.http.post<Computadora>(this.url + 'guardar/', compu); //Colocamos <Computadora> por que en nuestro endpoint nos devuelve un objeto de tipo Computadora
  }
  
}
