create table Refresco(
ID_Refresco int,
Nombre varchar(20),
Marca varchar(20),
Precio decimal(10,2),
primary key (ID_Refresco),
unique (Nombre, Precio) -- Estos atributos no permiten los mismo valores y si permite nulos
);

insert into Refresco values (1, "Mirinda", "Pepsi", 29.52),
							(2, "Delawer", "Coca cola", 25.99),
                            (3, "Limonada", "Peña fiel", 32.99);
                            
select * from Refresco;

-- ----------------------------------------------------------------------------------

create table Usuario(
ID_Usuario int auto_increment primary key,
Usuario varchar(30) unique, -- El valor del usuario no debe de repetirse
Nombre varchar(30),
email varchar(35)unique,	-- El valor de email no debe de repetirse
contraseña varchar(50) not null -- El valor de la contraseña no debe de quedar vacio
);

insert into Usuario (usuario, Nombre, email, contraseña) 
						values("Dany7","Dany","FELI@Gmail.com","1222r"),
							("Juan3","Juan","juan@Gmail.com","122r");
                            
select * from Usuario


