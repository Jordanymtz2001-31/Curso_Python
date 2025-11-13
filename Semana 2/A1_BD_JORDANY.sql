-- CREAMOS LA TABLA
 
create table Areas(
	Id_area int primary key,
    Nombre varchar(25),
    Gerente varchar(25)
);
use enucom;
drop table areas;

select * from Areas;

-- INSERTAMOS LOS DATOS A AREAS
insert into Areas values(1, "Limpieza", "Juan"),
						(2, "Carnes frias", "Maria"),
                        (3, "Panaderia", "Melany"),
                        (4, "Tecnologia", "Max");

-- CREAMOS LA TABLA DE PRODUCTOS
create table Productos (
	Id_Productos int auto_increment,
    Nombre varchar(25) unique,
    Marca varchar(25) default "No Definido",
    Precio decimal(10,2) not null,
    Area int,
    constraint Producto_PK primary key (Id_Productos),
    constraint Producto_FK foreign key (Area) references Areas(Id_area) 
);


-- INSERTAMOS LOS DATOS
insert into Productos (Nombre, Marca, Precio, Area) values("Gabon", "Blanca Nieves", 25, 1),
															("Papel", "Petalo", 30, 1),
                                                            ("Pechuga", "Fud", 120, 2),
                                                            ("Gamon", "Viva", 35, 2),
                                                            ("Pan tostado", "Bimbo", 30, 3),
                                                            ("Pan integral", "Rosseta", 35, 3),
                                                            ("Television", "LG", 7500, 4),
                                                            ("Bocina", "JGBL", 3500, 4),
                                                            ("Audifonos", "LG", 500, 4),
                                                            ("Laptop", "HP", 14500, 4);
                                                            
select * from productos;
                                                            
-- AGREGAR COLUMNA DE PROVEDOR A LA TABLA  PRODUCTOS Y POR DEFECTO "SER LOCAL"
alter table Productos add (Proveerdor varchar(25)default "LOCAL");

-- COLOCAR 5 PROVEEDORES EN PRODUCTOS
update Productos set Proveerdor = "Juan" 
where Id_Productos in (3,4,5);

update Productos set Proveerdor = "Martha" 
where Id_Productos in (8,6);

-- AGREGAR UNA RESTRICCION CHECK PRECIO > 25
alter table Productos add constraint Precio check (Precio >= 25);

insert into Productos (Nombre, Marca, Precio, Area) values("Cepillo", "Colgate", 20, 1), -- invalido
															("Telefono", "Huawei", 3000, 4); -- valido
														
-- ELIMINAR 2 AREAS EN USO
delete from Areas where Id_area = 1; -- Nose puede debo de eliminar primero los registros dependietes a este

delete from Productos where Id_Productos in (1,2);

-- ELIMINAR LA COLUMNA GERENTE
alter table Areas drop column Gerente;
select * from Areas;

-- ELIMINAR EL CAMPO DE AREA DE PRODUCTOS 
alter table Productos drop column Area; -- No me deja eliminarla, a menos que modifique o elimine la primary key original

alter table Productos drop foreign key Producto_FK;

