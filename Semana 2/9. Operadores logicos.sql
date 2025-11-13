create table Empleado(
	ID_Empleado int auto_increment primary key,
    Nombre varchar(25) not null,
    Departamento varchar(25),
    Salario decimal(10,2) not null,
    Fecha date not null
);

insert into Empleado(Nombre, Departamento, Salario, Fecha) values ("Juan Peres", "Ventas", 4500, "2025-04-21"),
																	("Maria Lopez", "Marqueting", 3500, "2024-04-20"),
                                                                    ("Rodrigo Peres", "TI", 4000, "2022-04-11"),
                                                                    ("Maria Alvarez", "Ventas", 6500, "2025-05-29"),
                                                                    ("Yos Martinez", null, 7500, "2025-07-01"),
                                                                    ("Luis Sanchez", "Ventas", 5300, "2025-04-21"),
                                                                    ("Fernando Solar", "Ventas", 4000, "2025-04-21");
                                                  
select * from Empleado;

-- AND
select * from Empleado where Departamento = "Ventas" and Salario > 4000;

-- OR
select * from Empleado where Departamento = "TI" or Salario = 3800;

-- BETWEEN
select * from Empleado where Salario between 4500 and 6000;

-- LIKE
select * from Empleado where Nombre Like "%L%";
select * from Empleado where Salario Like "4%";
select * from Empleado where Nombre Like "Ju________";

-- IN
select * from Empleado where Salario in (4500,6000);

-- NOT
select * from Empleado where NOT Salario in (4500,6000);

-- NOT NULL / IS NOT NULL
select * from Empleado where Departamento is null;
select * from Empleado where Departamento is not null;








