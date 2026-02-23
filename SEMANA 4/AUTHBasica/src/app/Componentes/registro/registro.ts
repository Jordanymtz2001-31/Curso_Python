import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../../Servidor/auth-service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-registro',
  imports: [FormsModule],
  templateUrl: './registro.html',
  styleUrl: './registro.css',
})
export class Registro {

  //Atributos para el formulario
  username = "";
  password = "";

  constructor(private auth: AuthService, private router: Router) { }

  registrar() {
    this.auth.registrar({ username: this.username, password: this.password }); //Llamamos al metodo registrar del servicio de autenticacion y le pasamos el nombre de usuario y la contraseña
    this.router.navigate(['/login']); //Redirigimos al usuario a la pagina de login
  }
}
