import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class ApiService {

  private url = 'http://localhost:8000/';
  
  //Creamos un constructor para inyectar 

  constructor(private http: HttpClient) { }

  getBienvenida() {
    return this.http.get<any>(this.url + 'bienvenida/');
  }

  getInfo() {
    return this.http.get<any>(this.url + 'informacion/');
  }

  getNoticias() {
    return this.http.get<any>(this.url + 'noticias/');
  }
}
