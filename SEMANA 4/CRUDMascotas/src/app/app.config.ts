import { ApplicationConfig, importProvidersFrom, provideBrowserGlobalErrorListeners, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { FormsModule } from '@angular/forms';
import { provideHttpClient } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(), //Esto funciona para mostrar el error de forma global
    provideZoneChangeDetection({eventCoalescing : true}), //Esto es para detectar los cambios, pero necesito Colocar en el Main.ts Zone.js
    provideRouter(routes),  //Esto funciona para las rutas
    importProvidersFrom([FormsModule]), //Esto es para usar formularios
    provideHttpClient() //Esto es para usar http
  ]
};
