import { Component, OnInit } from '@angular/core';
import { Servidor } from '../../Servidor/servidor';
import { Denominacion } from '../../Entidad/denominacion';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-dashboard',
  imports: [CommonModule],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css',
})
export class Dashboard implements OnInit {
  denominaciones: Denominacion[] = [];
  loading = false;
  error = '';

  constructor(private servidor: Servidor) {}

  ngOnInit(): void {
    this.cargarDenominaciones();
  }

  cargarDenominaciones() {
    this.loading = true;
    this.error = '';
    this.servidor.listarDenominaciones().subscribe({
      next: (data) => {
        this.denominaciones = data || [];
        this.loading = false;
      },
      error: (err) => {
        console.error('Error cargando denominaciones', err);
        this.error = 'No se pudieron cargar las denominaciones.';
        this.loading = false;
      },
    });
  }

  //Metodo para obtener el total de la caja
  getTotalCaja(): number {
    return this.denominaciones.reduce((s, d) => s + (d.valor * d.cantidad), 0);
  }

  //Metodo para inicializar el cajero
  inicializarCajero() {
    this.loading = true;
    this.error = '';
    this.servidor.inicializarCajero().subscribe({
      next: (data) => {
        this.cargarDenominaciones();
      },
      error: (err) => {
        console.error('Error inicializando cajero', err);
        this.error = 'No se pudo inicializar el cajero.';
        this.loading = false;
      },
    });
  }
}
