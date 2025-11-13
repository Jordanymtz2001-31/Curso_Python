create table Trabajadores(
	id_Trabajador int,
    Nombre varchar(20),
    Tipo varchar(25),
    Sueldo int,
    primary key (id_Trabajador)
);

insert into Trabajadores values (1, "Juan", "Plomero", 700),
								(2, "Matias", "Albañil", 600),
                                (3, "Lucas", "Carpintero", 500),
                                (4, "Maria", "Cochinera", 300),
                                (5, "Lupe", "Mesera", 200);
                                
select * from Trabajadores;

-- comando TCL para confirma
commit;

-- Si no cometemos un error en donde tenemos que modificar la tabla podemos modificarla
alter table Trabajadores rename column sueldo to salario;

-- Agregamos una nueva columna
alter table Trabajadores add (Horario varchar(40));

-- Agregamos datos a la nueva columna, pero hay que especificar bien
update Trabajadores set Horario = "14:00 - 20:00" 
where id_Trabajador in (1,2);

-- Modificar el tipo de datos
alter table Trabajadores modify salario decimal(10,2);

-- Agregar una restriccion
alter table Trabajadores add constraint Tipo unique (Tipo);

-- Eliminar una columna
alter table Trabajadores drop column Horario;

-- Eliminar una restriccion
alter table Trabajadores drop index Tipo;

-- En dado caso que borro toda la tabla por equivocacion
delete from Trabajadores;

-- Se usa el rollback
rollback;
select * from Trabajadores;
