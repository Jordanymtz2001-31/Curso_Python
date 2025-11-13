-- Formas de crear tablas con PK

-- --PRIMERA FORMA----
create table Botanas(
ID_Botana int primary key,
Nombre varchar (20),
Marca varchar (20)
);

-- --SEGUNDA FORMA----
create table Botanas(
ID_Botana int,
Nombre varchar (20),
Marca varchar (20),
primary key(ID_Botana)
);

-- --TERCERA FORMA----
create table Botanas(
ID_Botana int,
Nombre varchar (20),
Marca varchar (20),
constraint Botanas_PK primary key (ID_Botana)
);

insert into Botanas values 
(1, "Cheetos", "Sabritas"),
(2, "Papas", "Barcel"),
(3, "Donas", "Totis");

select * from Botanas