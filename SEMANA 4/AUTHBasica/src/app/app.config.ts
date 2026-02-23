import { ApplicationConfig, importProvidersFrom, provideBrowserGlobalErrorListeners, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { FormsModule } from '@angular/forms';
import { provideHttpClient, withInterceptors } from '@angular/common/http';
import { authInterceptor } from './interceptor/auth-interceptor';

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(), //Manejador de errores globales
    provideZoneChangeDetection({ eventCoalescing: true }), //Manejador de cambios de zona de Angular, Detección de cambios optimizada
    provideRouter(routes), //Manejador de rutas
    importProvidersFrom(FormsModule), //Manejador de formularios

    //Activa el sistema de peticiones http y le dice a angular que cada peticion tiene que pasar primero por el interceptor
    provideHttpClient(withInterceptors([authInterceptor])) //Le pasamos el interceptor que creamos
  ]
};
