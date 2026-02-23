import { Routes } from '@angular/router';
import { Listar } from './Componente/listar/listar';
import { Guardar } from './Componente/guardar/guardar';

export const routes: Routes = [

    {path: 'listar', component: Listar},
    {path: 'guardar', component: Guardar}
];
