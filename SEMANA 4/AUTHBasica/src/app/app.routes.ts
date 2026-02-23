import { Routes } from '@angular/router';
import { Bienvenida } from './Componentes/bienvenida/bienvenida';
import { Login } from './Componentes/login/login';
import { Registro } from './Componentes/registro/registro';
import { Info } from './Componentes/info/info';
import { authGuard } from './guards/auth-guard';
import { Noticias } from './Componentes/noticias/noticias';

export const routes: Routes = [

    //Rutas PUBLICAS
    {path: '' , component : Bienvenida}, //Indicamos que la ruta por defecto es Bienvenida
    {path: 'login', component: Login},
    {path: 'registro',  component: Registro},

    //Rutas protegidas
    {path: 'info', component: Info, canActivate: [authGuard]}, //Con el canActivate le indicamos que la ruta es protegida
    {path: 'noticias', component: Noticias, canActivate: [authGuard]}, // Es una proteccion e indica que antes de entrar a la ruta el guardia decide si se puede o no

    {path: '**', redirectTo: ''}, //Este es un comodin para redirigir cualquier ruta que no exista a la ruta por defecto
];
