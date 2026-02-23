import { ApplicationConfig, importProvidersFrom, provideBrowserGlobalErrorListeners } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { FormsModule } from '@angular/forms';
import { provideHttpClient } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(), // para capturar los errores globales
    provideRouter(routes), // para configurar las rutas
    importProvidersFrom(FormsModule), // para configurar los formularios
    provideHttpClient() // para configurar el http par las peticiones
  ]
};
