import { HttpClient, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Mascota } from '../Entidad/Mascota';

@Injectable({
  providedIn: 'root',
})
export class Servidor {

  //Inyectamos el Cliente HTTP en el constructor
  constructor(private http: HttpClient) {}

  //Creamos una variables para almacenar la URL
  url = 'http://localhost:8000/mascotas/';

  listar(): Observable<Mascota[]>{
    return this.http.get<Mascota[]>(this.url + 'listar_guardar/');
  }

  guardar(mascota: Mascota): Observable<HttpResponse<Mascota>>{  //Con HttpResponse podemos capturar el codigo de respuesta (Estatus, Body, Cabezera)
    return this.http.post<Mascota>(this.url + 'listar_guardar/', mascota , {observe: 'response'}); //Con observe: 'response' podemos capturar el codigo de respuesta de nuestra vista del back
  }

  editar(mascota: Mascota): Observable<HttpResponse<Mascota>>{
    return this.http.put<Mascota>(this.url + 'detalle/' + mascota.id + '/', mascota , {observe: 'response'});
  }

  //Void por que en el backend no nos regresa ningun dato, ni cuerpo
  eliminar(id : number): Observable<void>{
    return this.http.delete<void>(this.url + 'detalle/' + id + '/');
  }

  buscar(id: number): Observable<Mascota>{
    return this.http.get<Mascota>(this.url + 'detalle/' + id + '/');
  }
  
}
