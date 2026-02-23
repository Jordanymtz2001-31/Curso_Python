import { Component, OnInit } from '@angular/core';
import { Servidor } from '../../Servidor/servidor';
import { Denominacion } from '../../Entidad/denominacion';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-transacciones',
  imports: [CommonModule, FormsModule],
  templateUrl: './transacciones.html',
  styleUrl: './transacciones.css',
})
export class Transacciones implements OnInit {
  // RETIRAR
  retirarMonto: number | null = null; // monto ingresado por el usuario
  loadingRetirar = false;
  retirarResultado: any = null; // respuesta con "desglose" y "total"
  retirarError = '';

  // DEPOSITAR
  recargas: { valor: number; cantidad: number }[] = []; // items locales antes de enviar
  depositoValor: number | null = null;
  depositoCantidad: number | null = null;
  loadingDepositar = false;
  depositMsg = '';
  depositError = '';

  // Opcional: denominaciones actualizadas que devuelve el backend tras depositar
  denominacionesActualizadas: Denominacion[] = [];

  constructor(private servidor: Servidor) {}

  ngOnInit(): void {}

  // Ejecuta la llamada de retirar dinero al backend.
  // El backend espera { monto: number } y responde con {desglose: [...], total: number}
  ejecutarRetiro() {
    if (!this.retirarMonto || this.retirarMonto <= 0) { //Validamos el monto si no es valido
      this.retirarError = 'Ingresa un monto válido';
      return;
    }
    //Si son validos
    this.loadingRetirar = true; //Cambiamos el loading
    this.retirarError = ''; //Limpiamos el error
    this.retirarResultado = null; //Limpiamos el resultado

    // Llamamos al servicio que ahora envía {monto: ...}
    this.servidor.retirarDinero({ monto: this.retirarMonto }).subscribe({
      next: (res) => {
        // Se espera res = {desglose: [...], total: number}
        this.retirarResultado = res;
        this.loadingRetirar = false;
      },
      error: (err) => {
        console.error(err,'Error al retirar');
        this.retirarError = err.error?.error || 'Error al procesar retiro';
        this.loadingRetirar = false;
      },
    });
  }

  // Agrega una línea de recarga local (valor + cantidad)
  agregarRecarga() {
    if (!this.depositoValor || !this.depositoCantidad) return;
    this.recargas.push({ valor: this.depositoValor, cantidad: this.depositoCantidad }); // Agregamos la recarga a la lista
    this.depositoValor = null;
    this.depositoCantidad = null;
  }

  // Elimina una recarga local
  quitarRecarga(index: number) {
    this.recargas.splice(index, 1);
  }

  // Envia la recarga al backend: { recarga: [...] }
  ejecutarDepositar() {
    if (!this.recargas.length) { //Si no hay recargas entonces
      this.depositError = 'Agrega al menos una recarga antes de depositar.';
      return;
    }

    this.loadingDepositar = true;
    this.depositError = '';
    this.depositMsg = '';

    this.servidor.depositarDinero(this.recargas).subscribe({
      next: (res) => {
        // Respuesta esperada: { mensaje: 'Dinero agregado correctamente', denominaciones: [...] }
        this.depositMsg = res?.mensaje || 'Depósito realizado';
        // Normalizamos denominaciones si vienen con valores como strings
        if (res?.denominaciones) {
          this.denominacionesActualizadas = res.denominaciones.map((d: any) => ({
            ...d,
            valor: typeof d.valor === 'string' ? parseFloat(d.valor) : d.valor,
          }));
        }
        this.recargas = [];
        this.loadingDepositar = false;
      },
      error: (err) => {
        console.error('Error al depositar', err);
        this.depositError = err?.error?.mensaje || 'Error al procesar depósito';
        this.loadingDepositar = false;
      },
    });
  }

  // trackBy para listas (mejora rendimiento en *ngFor)
  trackByIndex(index: number, _item: any) {
    return index;
  }
}
