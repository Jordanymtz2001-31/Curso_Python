import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Denominacion } from '../Entidad/denominacion';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class Servidor {

  //Creamos un cosntrucctor para inicializar el servidor y inyectar las dependencias 
  constructor(private http : HttpClient) {}

  url = 'http://localhost:8000/cajero/'; //Creamos la ruta del servidor (Backend)
  
  //OBservable nos permite observar todo tipo de respuestas del servidor que mandamos
  //LA MEJOR PRACTICA ES USAR HttpResponse<T> para tipar la respuesta
  //si No sabemos el tipo de la respuesta usamos any para esperar lo que sea en la respuesta

  //Metodo para listar denominaciones
  listarDenominaciones(): Observable<Denominacion[]>{ //Observable nos permite observar todo tipo de respuestas, en este caso de la lista de denominaciones
    return this.http.get<Denominacion[]>(this.url + 'listar_denominaciones/');
  }

  //Metodo para inicializar el cajero
  inicializarCajero(): Observable<{mensaje: string}>{ //En este caso la respuesta es un mesaje del backend
    return this.http.post<{mensaje: string}>(this.url + 'inicializar_cajero/', {});
  }

    retirarDinero(retirar: {monto: number}): Observable<any>{ // any porque la respuesta puede variar (desglose, error...)
    const body = typeof retirar === 'number' ? { monto: retirar } : retirar; //Usamos una expresion ternaria para validar que el monto sea un number ya que el backend espera { monto: number }
    return this.http.post<any>(this.url + 'retirar_dinero/', body);
  }

  //Metodo para depositar dinero
  // El backend espera la forma: { "recarga": [ {valor:500, cantidad:1}, ... ] }
  depositarDinero(recarga : {valor: number, cantidad: number}[]): Observable<any>{ // any porque la respuesta puede incluir mensaje y lista de denominaciones
    return this.http.post<any>(this.url + 'depositar_dinero/', { recarga });
  }
}


