create table orders(
	ID_order int auto_increment primary key,
    Cliente varchar(30),
    Fecha_order date,
    Estatus varchar(30) default "Pendiente"
);

insert into orders (cliente, fecha_order, estatus) values ("Max","2025-10-05", "Enviando"),
															("Juan", "2024-05-22", "Rechazado");
                                                            
-- No metemos el valor estatus y si me lo acepta por que tiene un valor por default
insert into orders (cliente, fecha_order) values ("Maria", "2024-10-12");

select * from orders