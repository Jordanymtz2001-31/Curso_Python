-- 1. Creación de Tablas (DDL)

drop table CURSOS;
CREATE TABLE CURSOS(
id_curso INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(25) UNIQUE NOT NULL,
creditos INT DEFAULT 4,
profesor VARCHAR(25) NOT NULL
);

drop table ESTUDIANTES;
CREATE TABLE ESTUDIANTES(
	id_estudiante INT AUTO_INCREMENT,
	nombre VARCHAR(25) NOT NULL,
	matricula VARCHAR(20) UNIQUE NOT NULL,
	promedio DECIMAL(10,2) NOT NULL,
    id_curso INT,
    CONSTRAINT estudiante_pk PRIMARY KEY(id_estudiante),
	CONSTRAINT estudiante_fk FOREIGN KEY(id_curso) REFERENCES CURSOS(id_curso)
);

-- 2. Inserción de Datos (DML)

insert into CURSOS (nombre, creditos, profesor) values("Matemáticas", 2, "Juan"),
															("Física", 2, "Predro"),
                                                            ("Literatura", 2 , "Max"),
                                                            ("Historia", 1, "Lupe"),
                                                            ("Programación", 3, "Maria");
                                                            
insert into ESTUDIANTES (nombre, matricula, promedio, id_curso) values("Eduardo", "M1", 80.50, 1),
																		("Mario", "M2", 70.50, 2),
                                                                        ("Luis", "M3", 70.80, 3),
                                                                        ("Yos", "M4", 90.50, 4),
                                                                        ("Melany", "M5", 60.50, 5),
                                                                        ("Josue", "M6", 80.50, 1),
                                                                        ("Candido", "M7", 81.50, 1),
                                                                        ("Julia", "M8", 89.50, 3),
                                                                        ("Chely", "M9", 99.50, 5),
                                                                        ("Dany", "M11", 91.50, 3),
                                                                        ("Dylan", "M12", 76.50, 3),
                                                                        ("Isabel", "M13", 66.50, 3);
																	
-- 3. Modificación de Estructura (ALTER TABLE)
-- Agrega un campo correo a la tabla Estudiantes (DEFAULT 'sin_correo@escuela.com').
alter table ESTUDIANTES add (correo varchar(25)default "sin_correo@escuela.com");
SELECT * FROM ESTUDIANTES;


-- Agrega un campo horario a la tabla Cursos (DEFAULT 'Por asignar').
alter table CURSOS add (horario varchar(20) default "Por asignar");
SELECT * FROM CURSOS;

-- 4. Actualización de Datos (UPDATE)
-- Modifica el campo correo en 5 estudiantes (pon correos válidos).
UPDATE ESTUDIANTES
SET correo = CASE id_estudiante
    WHEN 1 THEN 'Edu@gmail.com'
    WHEN 3 THEN 'Luis@gmail.com'
    WHEN 5 THEN 'Melany@gmail.com'
    WHEN 7 THEN 'Candido@gmail.com'
    WHEN 9 THEN 'Chely@gmail.com'
    ELSE correo
END
WHERE id_estudiante IN (1,3,5,7,9);
SELECT * FROM ESTUDIANTES;

-- Modifica el campo horario en 3 cursos (ej. 'Lunes 9am', 'Martes 11am').
UPDATE CURSOS
SET horario = CASE id_curso
    WHEN 1 THEN 'Lunes 9am'
    WHEN 3 THEN 'Martes 8am'
    WHEN 5 THEN 'Viernes 8am'
    ELSE horario
END
WHERE id_curso IN (1,3,5);
SELECT * FROM CURSOS;

-- 5. Eliminación de Datos (DELETE)
-- Intenta eliminar un curso que tiene estudiantes asociados.
delete from CURSOS where id_curso = 1;
delete from ESTUDIANTES where id_estudiante in (1,6,7);

-- 6. Operación de Aumento de Promedio (UPDATE con Cálculo)
-- Aumenta en un 15% el promedio de todos los estudiantes del curso "Física".
UPDATE ESTUDIANTES as e
JOIN CURSOS  as c ON e.id_curso = c.id_curso
SET e.promedio =ROUND(e.promedio * 1.15)
WHERE c.nombre = 'Física';
SELECT * FROM ESTUDIANTES;

-- 7. Modificación Temporal y Reversión (Transacción)
-- Cambia el nombre de todos los estudiantes a 'NO IDENTIFICADO', y luego revierte el cambio usando transacciones.

START TRANSACTION;
-- Cambiar el nombre de todos los estudiantes
UPDATE ESTUDIANTES SET nombre = 'NO IDENTIFICADO'
WHERE id_estudiante BETWEEN 1 AND 12;
-- Aquí puedes verificar los cambios con un SELECT
SELECT * FROM estudiantes;
-- Si quieres revertir el cambio
ROLLBACK;
-- O si quieres confirmar el cambio
-- COMMIT;

-- 8. Eliminación de una Columna (ALTER TABLE)
-- Elimina la columna id_curso de la tabla Estudiantes.
alter table ESTUDIANTES drop column id_curso;
alter table ESTUDIANTES drop foreign key estudiante_fk;

																	

-- Extra: Consultas Adicionales (Práctica de SELECT)
-- Lista cursos con más de 4 créditos.
SELECT * FROM CURSOS
WHERE CREDITOS > 2;

-- Muestra estudiantes con promedio mayor al promedio general (subconsulta). - opcional
SELECT *FROM ESTUDIANTES
WHERE promedio > (SELECT AVG(promedio) FROM ESTUDIANTES);


