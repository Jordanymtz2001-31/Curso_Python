import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private url = 'http://localhost:8000/';

  constructor(private http: HttpClient) { }

  //Metodo para registrarse 
  registrar(data: any) {
    return this.http.post(this.url + 'registrar/', data);
  }

  //Metodo para loguearse
  loging(username: string, password: string) {
    //boat convierte las credenciales en base 64
    //La autenticacion basica necesita el formato username:password codificado en base 64
    const credenciales = btoa(`${username}:${password}`);
    localStorage.setItem('auth', credenciales); //Guardamos las credenciales en el almacenamiento del navegador
  }

  logout() {
    //Eliminamos las credenciales del almacenamiento del navegador (Lo deslogueamos)
    localStorage.removeItem('auth');
  }
  
  //Metodo para saber si el usuario esta autenticado
  isLogged(): boolean {
    //Comprobamos si el almacenamiento del navegador tiene credenciales
    //Si es diferente de null quiere decir que el usuario esta autenticado
    //Si es null quiere decir que el usuario no esta autenticado
    return localStorage.getItem('auth') !== null;
  }

  //Metodo para obtener las credenciales almacenadas en el navegador
  //Este metodo lo usa el interceptor para la cabecera Authorization Basic
  getAuth() {
    return localStorage.getItem('auth');
  }
}
