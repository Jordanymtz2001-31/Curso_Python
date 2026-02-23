import { ApplicationConfig, importProvidersFrom, provideBrowserGlobalErrorListeners, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { FormsModule } from '@angular/forms';
import { provideHttpClient } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(), //Configuracion para capturar los errores globales
    provideRouter(routes), //Configuracion para las rutas
    provideZoneChangeDetection({eventCoalescing: true}), //Deteccion de cambios optimizada
    importProvidersFrom(FormsModule), //Importamos el modulo de formularios
    provideHttpClient()
  ]
};
