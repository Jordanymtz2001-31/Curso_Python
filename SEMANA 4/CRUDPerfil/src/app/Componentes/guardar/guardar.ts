import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { Servidor } from '../../Servidor/servidor';
import { Perfil } from '../../Entidad/perfil';

@Component({
  selector: 'app-guardar',
  imports: [FormsModule],
  templateUrl: './guardar.html',
  styleUrl: './guardar.css',
})
export class Guardar {
  // Inyectamos el router y el servidor
  constructor(private router: Router, private service: Servidor) {}

  // Intancia de la clase Perfil
  perfil: Perfil = new Perfil();

  guardar() {
    this.service.guardarPerfil(this.perfil).subscribe(() => {
      this.router.navigate(['listar']);
    });
  }

  cancelar() {
    this.router.navigate(['listar']);
  }
}
