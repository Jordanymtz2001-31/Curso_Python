import { HttpInterceptorFn } from '@angular/common/http';

export const authInterceptor: HttpInterceptorFn = (req, next) => {

  const auth = localStorage.getItem('auth'); //Obtenemos las credenciales codificadas almacenadas en el almacenamiento del navegador

  //Validamos si tenemos credenciales
  if (auth) {
    const authRequest = req.clone({ //Clonamos la peticion y le anadimos la cabecera Authorization Basic

      //Agregamos la cabecera de autenticacion a la peticion clonada
      setHeaders: {
        Authorization: `Basic ${auth}`
      }
    });
    //Retornamos la peticion clonada
    return next(authRequest);
  }
  //Si no existe las credenciales, mandamos la peticion orriginal
  return next(req);
};
