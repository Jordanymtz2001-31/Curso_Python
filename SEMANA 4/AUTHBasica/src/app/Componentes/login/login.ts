import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../../Servidor/auth-service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  imports: [FormsModule],
  templateUrl: './login.html',
  styleUrl: './login.css',
})
export class Login {

  username = ''; //Variable para almacenar el nombre de usuario
  password = ''; //Variable para almacenar la contraseña

  constructor(private auth: AuthService, private router: Router) { }

  login() { //Metodo para loguearse
    this.auth.loging(this.username, this.password); //Llamamos al metodo loging del servicio de autenticacion y le pasamos el nombre de usuario y la contraseña
    this.router.navigate(['/']); //Redirigimos al usuario a la pagina de info
  }

}
