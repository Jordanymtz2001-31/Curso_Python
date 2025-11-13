create table libros(
	ID_libro int not null,
    Libro varchar(50),
    Autor varchar (50),
    Año int,
    Precio decimal (10,2),
    Editorial varchar(20),
    primary key (ID_libro, Editorial)
);

insert into libros values (1,"Libro 1", "Autor 1", 2020, 200.99, "Editorial 1"),
							(2,"Libro 2", "Autor 2 ", 2021, 300.99, "Editorial 2"),
                            (3, "Libro 3", "Autor 3", 2022, 280.99, "Editorial 3"),
                            (4, "Libro 4", "Autor 4", 2023, 120.99, "Editorial 4");
                            
insert into libros values (3,"Libro 1", "Autor 1", 2020, 200.99, "Editorial 1");

select * from libros
															
