import { Routes } from '@angular/router';
import { Dashboard } from './Componentes/dashboard/dashboard';
import { Transacciones } from './Componentes/transacciones/transacciones';

export const routes: Routes = [

    { path: '', redirectTo: '/dashboard', pathMatch: 'full' }, //Ruta por defecto al iniciar
    {path: 'dashboard', component: Dashboard},
    {path: 'transacciones', component: Transacciones},
    { path: '**', redirectTo: '/dashboard' } //Ruta por defecto al iniciar en caso de que la ruta no exista

];
