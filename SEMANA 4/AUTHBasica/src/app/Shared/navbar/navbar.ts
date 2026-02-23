import { Component } from '@angular/core';
import { Router, RouterLink, RouterModule } from "@angular/router";
import { AuthService } from '../../Servidor/auth-service';

@Component({
  selector: 'app-navbar',
  imports: [RouterLink, RouterModule],
  templateUrl: './navbar.html',
  styleUrl: './navbar.css',
})
export class Navbar {

  //Creamos un constructor para inyectar el servicio de rutas y la autenticacion
  constructor(private router: Router, public auth: AuthService) { } //Colocamos como publico el servicio de autenticacion para usar el metodo logout

  //Metodo para cerrar sesion
  logout() {
    this.auth.logout(); //Llamamos al metodo logout del servicio de autenticacion
    this.router.navigate(['/']); //Redirigimos al usuario a la pagina de login
  }

}
