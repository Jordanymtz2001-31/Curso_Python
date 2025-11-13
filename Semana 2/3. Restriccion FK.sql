create table Auto(
ID_Auto int,
Modelo varchar(30),
Kilometraje int, 
Tamaño varchar (15),
Marca int,
constraint Auto_PK primary key (ID_Auto),
constraint Auto_FK foreign key (Marca) references Marcas(ID_Marca) 
);

create table Marcas(
ID_Marca int primary key,
nombre varchar (30)
);

insert into Marcas values(1, "marca 1"),
						(2, "marca 2"),
                        (3, "marca 3");
                        
insert into Auto values(1, "modelo 1", 500, "Grande", 1),
						(2, "modelo 2", 800, "Mediano", 2),
                        (3, "modelo 3", 400, "Pequeño", null);
                        
select * from Marcas;
select * from Auto;

-- Eliminacion
delete from auto where ID_Auto = 3;

-- Eliminacion donde primero hay que eliminar las referencias
delete from auto where Marca = 1;
delete from marcas where ID_Marca = 1;
                        
                        
                    
