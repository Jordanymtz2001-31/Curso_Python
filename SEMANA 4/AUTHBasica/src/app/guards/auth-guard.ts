import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from '../Servidor/auth-service';

//El guardia protege las plantillas de las rutas para que solo se puedan acceder si el usuario esta autenticado
export const authGuard: CanActivateFn = (route, state) => {

  const auth = inject(AuthService); //Inyectamos el servicio de autenticacion
  const router = inject(Router); //Inyectamos el servicio de rutas

  if (auth.isLogged()) { //Comprobamos si el usuario esta autenticado
    return true;
  }else{
    //Si el usuario no esta autenticado lo redirigimos a la pagina de login
    router.navigate(['/login']);
  return false;
  }
};
