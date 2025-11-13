import { Routes } from '@angular/router';
import { Listar } from './Componentes/listar/listar';
import { Guardar } from './Componentes/guardar/guardar';

export const routes: Routes = [
  {
    path: 'listar',
    component: Listar,
  },
  {
    path: 'guardar',
    component: Guardar,
  },
];
