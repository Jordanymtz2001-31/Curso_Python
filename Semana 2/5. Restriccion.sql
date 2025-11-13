create table Produtos(
ID_Producto int auto_increment primary key,
Nombre varchar (30) not null,
Precio decimal(10, 2)not null,
constraint precio check(Precio > 10) -- Hacemos validaciones que le precio sea mayor a 10
);
drop table produtos;

select * from Produtos;

insert into Produtos (Nombre, Precio) values ("Cepillo",19.99), ("Gel",40.99), ("Papas", 20.99)
