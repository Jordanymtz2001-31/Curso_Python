create database ENUCOM;
USE ENUCOM;

create table Persona(
Id_Persona int,
Nombre varchar(15),
Estado varchar(20),
Edad int 
);

select * from Persona;

insert into Persona values (1, "Dany", "Mexico", 22),
							(2, "Juan", "Puebla", 27),
                            (3, "Melany", "Tabasco", 23),
                            (4, "Max", "Veracruz", 40)