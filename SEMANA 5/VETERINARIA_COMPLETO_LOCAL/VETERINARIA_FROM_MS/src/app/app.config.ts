import { ApplicationConfig, importProvidersFrom, provideBrowserGlobalErrorListeners, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { FormsModule } from '@angular/forms';
import { provideHttpClient } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(), // Provee manejo global de errores 
    provideZoneChangeDetection({ eventCoalescing: true }), // Mejora la detección de cambios
    provideRouter(routes), // Provee las rutas de la aplicación
    importProvidersFrom(FormsModule), // Importa FormsModule para formularios
    provideHttpClient() // Importa HttpClient para solicitudes HTTP
  ]
};
