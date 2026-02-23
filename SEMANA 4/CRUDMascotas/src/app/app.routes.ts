import { Routes } from '@angular/router';
import { Listar } from './Componentes/listar/listar';
import { Guardar } from './Componentes/guardar/guardar';
import { Editar } from './Componentes/editar/editar';

export const routes: Routes = [

    {path: 'listar', component: Listar},
    {path: 'guardar', component: Guardar},
    {path: 'editar', component: Editar}
];
