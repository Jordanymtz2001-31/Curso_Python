-- CREACION DE TABLAS

CREATE TABLE Materia (
  id_materia INT PRIMARY KEY,
  nombre VARCHAR(20),
  semestre INT,
  creditos INT,
  costo_credito DECIMAL(10,2),
  docente INT
);

CREATE TABLE Alumnos_A (
  id_alumno INT PRIMARY KEY,
  nombre VARCHAR(20),
  edad INT,
  materia_id INT,
  carrera INT
);	

-- INSERTAMOS LOS VALORES
INSERT INTO Materia VALUES
(1, 'Matematicas', 1, 6, 100.00, 1),
(2, 'Programacion', 2, 5, 120.00, 2),
(3, 'Electronica Basica', 3, 4, 110.00, 3),
(4, 'Anatomia', 1, 7, 130.00, 4),
(5, 'Derecho Civil', 2, 3, 90.00, 2);

INSERT INTO Alumnos_A VALUES
(1, 'Ana', 20, 1, 1),
(2, 'Luis', 22, 2, 2),
(3, 'Marta', 19, 3, 3),
(4, 'Jorge', 21, NULL, 2),
(5, 'Sofia', 23, 1, 1),
(6, 'Pedro', 20, 4, 4),
(7, 'Carla', 22, NULL, 5);

SELECT * FROM Alumnos_A;

-- CONSULTAS --
-- 1.- Mostrar los registros de alumnos con sus respectivas materias. Agregar los nombres de las carrer
SELECT 
  a.id_alumno, 
  a.nombre AS alumno,
  m.nombre AS materia,
  CASE a.carrera
    WHEN 1 THEN 'Sistemas'
    WHEN 2 THEN 'Informatica'
    WHEN 3 THEN 'Electronica'
    WHEN 4 THEN 'Medicina'
    WHEN 5 THEN 'Derecho'
    ELSE 'Otro'
  END AS nombre_carrera
FROM Alumnos_A a
LEFT JOIN Materia m ON a.materia_id = m.id_materia;

SELECT a.id_alumno, a.nombre AS alumno, m.nombre AS materia
FROM Alumnos a
LEFT JOIN Materia m ON a.materia_id = m.id_materia;

-- 2.- Contar cuantos alumnos existen por materia. 
SELECT m.nombre, COUNT(a.id_alumno) as Total_alumno
FROM materia m 
LEFT JOIN Alumnos_A a ON m.id_materia = a.materia_id
GROUP BY m.id_materia;

-- 3.- Mostrar la materia con mayor numero de creditos y agregar la palabra creditos al resultado.
SELECT nombre, CONCAT(creditos, ' creditos') AS creditos
FROM Materia
ORDER BY creditos DESC
LIMIT 1;


-- 4.- Mostrar el docente y su numero de materias. 
SELECT
( 
	CASE docente
		WHEN 1 THEN "Francisco Hernandez"
        WHEN 2 THEN "EDUARDO SALAZAR "	
        WHEN 3 THEN "Daniel Jimenez "	
        WHEN 4 THEN "Jimena Gonzales "	
        ELSE "Otro"
	END
)AS Nombres,
COUNT(*) AS Numero_Materias
FROM Materia
GROUP BY Docente;

--   5.- Mostrar el docente que imparte mas materias.
SELECT
  CASE docente
    WHEN 1 THEN 'Francisco Hernandez'
    WHEN 2 THEN 'Eduardo Salazar'
    WHEN 3 THEN 'Daniel Jimenez'
    WHEN 4 THEN 'Jimena Gonzales'
    ELSE 'Otro'
  END AS nombre_docente,
  COUNT(*) AS numero_materias
FROM Materia
GROUP BY docente
ORDER BY numero_materias DESC
LIMIT 1;

--   6.- Mostrar el docente que imparte menos materias.
SELECT
  CASE docente
    WHEN 1 THEN 'Francisco Hernandez'
    WHEN 2 THEN 'Eduardo Salazar'
    WHEN 3 THEN 'Daniel Jimenez'
    WHEN 4 THEN 'Jimena Gonzales'
    ELSE 'Otro'
  END AS nombre_docente,
  COUNT(*) AS numero_materias
FROM Materia
GROUP BY docente
ORDER BY numero_materias ASC
LIMIT 1;


-- 7.- Ordenar las materias por su nombre y luego por sus creditos en una sola consulta.
SELECT nombre, creditos FROM Materia
ORDER BY nombre ASC, creditos ASC;

-- 8.- Ordenar los alumnos por su nombre y luego por su edad en una sola consulta
SELECT nombre, edad FROM Alumnos_A
ORDER BY nombre ASC, edad ASC;

-- 9.- Sacar el total de creditos por alumnos de acuerdo a las materias que esta cursando.
SELECT a.id_alumno, a.nombre AS alumno, 
COALESCE(SUM(m.creditos), 0) AS total_creditos
FROM Alumnos_A a
LEFT JOIN Materia m ON a.materia_id = m.id_materia
GROUP BY a.id_alumno, a.nombre;

-- 10.- Mostrar el alumno que curse mas materias. 
SELECT a.id_alumno, a.nombre as Alumno,
COUNT(m.id_materia) AS TOTAL_MATERIAS
FROM Alumnos a
LEFT JOIN Materia m ON a.materia_id = m.id_materia
GROUP BY a.id_alumno, a.nombre
ORDER BY COUNT(m.id_materia) DESC
LIMIT 1;

-- 11.- Mostrar los alumnos que no estan tomando materias.
SELECT a.id_alumno, a.nombre as Alumno,
COUNT(m.id_materia) AS TOTAL_MATERIAS
FROM Alumnos a
LEFT JOIN Materia m ON a.materia_id = m.id_materia
GROUP BY a.id_alumno, a.nombre
ORDER BY COUNT(m.id_materia) ASC
LIMIT 1;


-- 12.- Mostrar las materias que no estan siendo impatidas
SELECT nombre FROM Materia
WHERE id_materia NOT IN 
(SELECT DISTINCT materia_id FROM Alumnos WHERE materia_id IS NOT NULL);

-- 13.- Mostrar el costo total de creditos por alumnos con formato.
SELECT a.nombre,
FORMAT(COALESCE(SUM(m.creditos * m.costo_credito), 0), 2) AS costo_total
FROM Alumnos a
LEFT JOIN Materia m ON a.materia_id = m.id_materia
GROUP BY a.id_alumno
ORDER BY costo_total DESC;

-- 14.- Mostrar el alumno que paga mas con formato. 
SELECT a.nombre,
FORMAT(SUM(m.creditos * m.costo_credito),2) AS pago_maximo
FROM Alumnos a
LEFT JOIN Materia m ON a.materia_id = m.id_materia
GROUP BY a.id_alumno
ORDER BY pago_maximo DESC
LIMIT 1;

-- 15.- Mostrar el alumno que paga menos con formato.
SELECT a.nombre,
FORMAT(SUM(m.creditos * m.costo_credito),2) AS pago_minimo
FROM Alumnos a
LEFT JOIN Materia m ON a.materia_id = m.id_materia
GROUP BY a.id_alumno
ORDER BY pago_minimo ASC
LIMIT 1;

-- 16.- Calcula el año de nacimiento de cada alumno.
SELECT nombre, YEAR(CURDATE()) - edad AS anio_nacimiento
FROM Alumnos;

-- 17.- Calcula la fecha de egreso por alumno dependiento del semestre que cursa con
-- la materia asumiendo que dura 10 semestres la carrera y asumiendo que inicia en la fecha actual. 
SELECT a.nombre,
DATE_ADD(CURDATE(), INTERVAL (10 - m.semestre) * 6 MONTH) AS fecha_egreso
FROM Alumnos a
LEFT JOIN Materia m ON a.materia_id = m.id_materia;


-- 18.- Calcula la fecha de ingreso del alumno a partir del semestre de la materia
-- asumiendo que inicia en la fecha actual.
SELECT a.nombre,
DATE_SUB(CURDATE(), INTERVAL (m.semestre - 1) * 6 MONTH) AS fecha_ingreso
FROM Alumnos a
LEFT JOIN Materia m ON a.materia_id = m.id_materia;



























