-- TABLA DE MASCOTAS
USE ENUCOM;
CREATE TABLE Mascotas (
  id_mascota INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  especie VARCHAR(255) NOT NULL,
  raza VARCHAR(255) DEFAULT 'mestizo',
  fecha_nacimiento DATE NOT NULL,
  fecha_registro DATE DEFAULT (CURDATE())
);
SELECT * FROM Mascotas;
DROP TABLE Mascotas;
-- TABLA CLIENTES
CREATE TABLE Clientes_V (
  id_cliente INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  contacto VARCHAR(255) UNIQUE,
  direccion VARCHAR(255) NOT NULL
);
-- TABLA VISITAS
CREATE TABLE Visitas (
  id_visita INT AUTO_INCREMENT PRIMARY KEY,
  id_mascota INT,
  fecha_visita DATE NOT NULL UNIQUE,
  motivo VARCHAR(255),
  costo DECIMAL(10, 2),
  id_cliente INT,
  CONSTRAINT VISITAS_fk_mascota FOREIGN KEY (id_mascota) REFERENCES Mascotas(id_mascota),
  CONSTRAINT VISITAS_fk_cliente FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);

-- Mascotas
INSERT INTO Mascotas (nombre, especie, raza, fecha_nacimiento) VALUES
('Bobby', 'Perro', 'Labrador', '2022-05-01'),
('Bella', 'Perro', NULL, '2020-07-15'),
('Coco', 'Gato', 'Siames', '2023-02-10'),
('Mimi', 'Gato', NULL, '2021-11-20'),
('Luna', 'Perro', 'Beagle', '2023-04-25'),
('Pipo', 'Gato', 'Persa', '2024-01-05'),
('Bruno', 'Perro', 'Bulldog', '2019-09-09');

-- Clientes
INSERT INTO Clientes_V (nombre, contacto, direccion) VALUES
('Juan Perez', 'juanp@example.com', 'Calle Luna 123'),
('Ana Gomez', 'ana@example.com', 'Avenida Sol 456'),
('Luis Rojo', 'luisr@example.com', 'Calle Mar 789'),
('Marta Diaz', 'marta@example.com', 'Plaza Central'),
('Carlos Ruiz', 'carlosr@example.com', 'Calle Estrella 321'),
('Sofia Molina', 'sofia@example.com', 'Avenida Paz 654'),
('Pedro Alvarez', 'pedro@example.com', 'Calle Olmo 987');

-- Visitas
INSERT INTO Visitas (id_mascota, fecha_visita, motivo, costo, id_cliente) VALUES
(1, '2025-01-10', 'Vacunación', 600, 1),
(2, '2025-02-14', 'Consulta general', 300, 2),
(3, '2025-07-20', 'Vacunación', 550, 3),
(4, '2025-08-18', 'Desparasitación', 200, 4),
(5, '2025-09-05', 'Chequeo', 700, 5),
(6, '2025-09-30', 'Vacunación', 650, 6),
(7, '2025-10-01', 'Consulta general', 250, 7);

SELECT * FROM Visitas;


-- Seleccionar todas las mascotas cuyo nombre empiece con la letra 'B' y cuya especie sea 'Perro'.
SELECT * FROM Mascotas 
WHERE nombre LIKE 'B%' AND especie = 'Perro';

-- Seleccionar las visitas que hayan ocurrido en los últimos 10 meses y cuyo costo sea mayor a 500.
SELECT * FROM Visitas
WHERE fecha_visita >= DATE_SUB(CURDATE(), INTERVAL 10 MONTH) AND costo > 500;

-- Seleccionar las mascotas que sean 'Gato' y cuyo motivo de consulta sea 'Vacunación'.
SELECT *
FROM Mascotas
WHERE especie = 'Gato'
  AND id_mascota IN (
    SELECT id_mascota
    FROM Visitas
    WHERE motivo = 'Vacunación'
  );

-- Calcular el costo promedio de todas las visitas.
SELECT AVG(costo) AS costo_promedio FROM Visitas;

-- Mostrar el total de visitas registradas.
SELECT COUNT(*) AS total_visitas FROM Visitas;

-- Encontrar la visita con el menor costo.
SELECT * FROM Visitas 
WHERE costo = (SELECT MIN(costo) FROM Visitas);

-- Encontrar la visita con el mayor costo.
SELECT * FROM Visitas 
WHERE costo = (SELECT MAX(costo) FROM Visitas);

-- Mostrar los nombres de todas las mascotas en mayúsculas.
SELECT UPPER(nombre) AS nombre_mayus FROM Mascotas;

-- Mostrar los nombres de todas las mascotas en minúsculas.
SELECT LOWER(nombre) AS nombre_minus FROM Mascotas;

-- Seleccionar los clientes cuya dirección contenga la palabra 'calle'.
SELECT * FROM Clientes 
WHERE direccion LIKE '%calle%';

-- Mostrar los primeros 4 caracteres del nombre del cliente.
SELECT nombre, SUBSTRING(nombre, 1, 4) AS primeros_4 FROM Clientes;

-- Mostrar la cantidad de caracteres del nombre de la mascota.
SELECT nombre, CHAR_LENGTH(nombre) AS longitud FROM Mascotas;

-- Mostrar las mascotas que nacieron en los últimos 2 años.
SELECT * FROM Mascotas 
WHERE fecha_nacimiento >= DATE_SUB(CURDATE(), INTERVAL 2 YEAR);

-- Mostrar todas las visitas realizadas en el año actual.
SELECT * FROM Visitas 
WHERE YEAR(fecha_visita) = YEAR(CURDATE());

-- Mostrar las visitas que ocurrieron en fin de semana.
SELECT * FROM Visitas 
WHERE DAYOFWEEK(fecha_visita) IN (1, 7);


-- Calcular el costo promedio de las visitas de mascotas cuyo nombre comience con 'P' 
-- y que hayan nacido después del año 2023.
SELECT AVG(costo) AS costo_promedio
FROM Visitas
WHERE id_mascota IN (
    SELECT id_mascota
    FROM Mascotas
    WHERE nombre LIKE 'P%'
      AND fecha_nacimiento > '2023-01-01'
);


-- Mostrar todas las visitas realizadas en el mes de febrero y cuyo costo sea mayor a 250.
SELECT * FROM Visitas
WHERE MONTH(fecha_visita) = 2 AND costo > 250;


-- Mostrar todas las mascotas registradas en los últimos 30 días.
SELECT * FROM Mascotas 
WHERE fecha_registro >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);

-- Mostrar las visitas realizadas en los primeros 5 días de cualquier mes.
SELECT * FROM Visitas WHERE DAY(fecha_visita) <= 5;




