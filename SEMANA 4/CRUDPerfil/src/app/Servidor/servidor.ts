import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Perfil } from '../Entidad/perfil';

@Injectable({
  providedIn: 'root',
})
export class Servidor {
  // Inyectamos el client http
  constructor(private http: HttpClient) {}

  // Ruta de acceso al backend
  url = 'http://localhost:8000/perfil/';

  // Metodos para la comunicacion back - front
  listarPerfil() {
    return this.http.get<Perfil[]>(this.url + 'listar/');
  }

  guardarPerfil(perfil: Perfil) {
    return this.http.post<Perfil>(this.url + 'guardar/', perfil);
  }
} 
