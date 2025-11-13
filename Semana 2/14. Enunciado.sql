CREATE TABLE CURSOS_C(
	ID_CURSO INT PRIMARY KEY,
    NOMBRE VARCHAR(25),
    CREDITOS INT
);

drop table ESTUDIANTE_C;
CREATE TABLE ESTUDIANTE_C(
	ID_ESTUDIANTE INT AUTO_INCREMENT PRIMARY KEY,
    NOMBRE VARCHAR(25),
    APELLIDO VARCHAR(20),
    FECHA DATE,
    PROMEDIO DECIMAL(3,1),
    ID_CURSO INT,
    foreign key (ID_CURSO) REFERENCES CURSOS_C(ID_CURSO)
    );

USE enucom;

INSERT INTO ESTUDIANTE_C (NOMBRE,  APELLIDO, FECHA, PROMEDIO, ID_CURSO) VALUES
																		("Eduardo", "GARCIA", "2000-05-23", 9.5,1),
																		("Mario", "MARTINEZ", "1999-02-20", 6.8, 2),
                                                                        ("Luis", "ARIAS", "2002-09-01", 7.6,3),
                                                                        ("Yos", "GONZALEZ", "2006-11-25", 8.6, 4),
                                                                        ("Melany", "PEREZ", "2003-05-24", 9.1, 2),
                                                                        ("Josue", "RAMIREZ", "2009-12-30", 8.8, 2),
                                                                        ("Candido", "HERNANDEZ", "1998-08-18", 7.6, 3),
                                                                        ("Julia", "JUAREZ", "2008-08-28", 7.6, 3),
                                                                        ("Chely", "ARIAS", "2001-04-24", 9.6, 4),
                                                                        ("Dany", "GARCIA", "2006-08-19", 6.9, 1),
                                                                        ("Dylan", "MARTINEZ", "2004-01-20", 7.0, 2),
                                                                        ("Isabel", "LOPEZ", "2012-02-03", 8.0, 2);
									
INSERT INTO CURSOS_C  VALUES(1, "ALGEBRA", 6),
							(2, "HISTORIA", 5),
							(3, "MATEMATICAS", 6),
							(4, "CIVICA", 4);
                            
select *  FROM CURSOS_C;
                            
-- Obtener el número total de estudiantes inscritos.
SELECT COUNT(*) AS TOTAL_ESTUDIANTE FROM ESTUDIANTE_C;

-- Calcular el promedio general de calificaciones.
SELECT FORMAT(AVG(PROMEDIO),2) PROMEDIO_GENERAL FROM ESTUDIANTE_C;

-- Listar los nombres completos de los estudiantes en mayúsculas junto con su edad actual.
SELECT UPPER(NOMBRE) AS NOMBRE, UPPER(APELLIDO) AS APELLIDO,
timestampdiff(YEAR, FECHA, CURDATE()) AS EDAD
FROM ESTUDIANTE_C;

-- Mostrar el nombre completo del estudiante y la longitud de su nombre completo
SELECT CONCAT(NOMBRE, "" , APELLIDO) AS NOMBRE_COMPLETO,
LENGTH(CONCAT(NOMBRE, "" , APELLIDO)) AS LONGITUD 
FROM ESTUDIANTE_C;

-- Listar los cursos con más de 4 créditos.
SELECT * FROM CURSOS_C WHERE CREDITOS > 4;

-- Contar cuántos estudiantes tienen calificación redondeada mayor o igual a 9.
SELECT ESTUDIANTE_C 
WHERE ROUND(PROMEDIO) >= 9;

SELECT AVG(PROMEDIO) FROM ESTUDIANTE_C;

-- Concatenar nombre y apellido de los estudiantes en una sola columna llamada nombre_completo.
SELECT CONCAT(NOMBRE, "  "  ,APELLIDO) AS NOMBRE_COMPLETO
FROM ESTUDIANTE_C;

-- Mostrar la cantidad de días que han pasado desde la fecha de nacimiento de cada estudiante hasta hoy.
SELECT NOMBRE, APELLIDO, FECHA, CURDATE() AS FEHCA_ACTUAL,
DATEDIFF(CURDATE(), FECHA) AS DIAS_VIVIDOS
FROM ESTUDIANTE_C;

SELECT NOMBRE, APELLIDO, FECHA, CURDATE() AS FEHCA_ACTUAL,
TIMESTAMPDIFF(DAY, FECHA, CURDATE()) AS DIAS_VIVIDOS
FROM ESTUDIANTE_C;

-- Contar cuántos estudiantes nacieron en cada mes del año (función de fecha + GROUP BY).
SELECT MONTHNAME(FECHA) AS MES, COUNT(*) AS TOTAL
FROM ESTUDIANTE_C
GROUP BY MES
ORDER BY month(FECHA)





