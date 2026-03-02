import { AfterViewInit, Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { Servidor } from '../../../Servidor/servidor';
import { Clientes } from '../../../Entidad/clientes';

@Component({
  selector: 'app-listar-c',
  imports: [FormsModule, CommonModule], //CommonModule para usar ngIf y ngFor
  templateUrl: './listar-c.html',
  styleUrl: './listar-c.css',
})
//El OnInit es un ciclo de vida del componente que se ejecuta al iniciar el componente
//El AfterViewInit es un ciclo de vida del componente que se ejecuta despues de que la vista se ha inicializado
export class ListarC  implements OnInit, AfterViewInit {

  constructor(private router:Router, private servidor: Servidor) { }

  // Crear una lista para almacenar los clientes
  clientes!: Clientes[];
  loading = true;
  cliente = new Clientes();


  // El metodo ngAfterViewInit se ejecuta despues de que la vista se ha inicializado
  ngAfterViewInit(): void {
    setTimeout (() => {
      const section = document.getElementById('clientes-section');
      section?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 200);
  }

  // El metodo ngOnInit se ejecuta al iniciar el componente
  ngOnInit(): void {
    this.servidor.listarClientes().subscribe({
      next: (data: any) => {
        this.clientes = Array.isArray(data) ? data : [data];
        this.loading = false;
      },
      error: (err) => {
        console.error('Error al cargar los clientes', err);
        this.loading = false;
      },
    });
  }

  eliminarCliente(id : number){
    if(confirm('¿Esta seguro de que quiere eliminar el cliente?')){
      this.servidor.eliminarCliente(id).subscribe({
        next: () => {
          // Actualizar la lista de clientes despues de eliminar uno
          this.clientes = this.clientes.filter((c) => c.id_cliente !== id);
        },
        error: (err) => console.error('Error  al eliminar al cliente:', err),
      })
    }
  }

  volverInicio(){
    this.router.navigate(['/']).then(() => {
      const menu = document.getElementById('menu-section');
      menu?.scrollIntoView({behavior: 'smooth', block: 'start'});
    });
  }
  //metodo para editar cliente
  editarCliente(id: number){
    this.router.navigate(['editar-cliente', id]);
  }
}
