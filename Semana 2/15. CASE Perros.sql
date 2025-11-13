use enucom;

CREATE TABLE PERROS(
	ID_PERRO INT PRIMARY KEY,
    NOMBRE VARCHAR(20), 
    COLOR VARCHAR(25),
    RAZA INT, 
    PESO INT
);

INSERT INTO PERROS VALUES
(1,"DUQUE", "CAFE OSCURO", 1, 25),
(2, "SAM", "CAFE CLARO", 1, 30),
(3, "WILI", "BANCO", 3, 20), 
(4, "BETO", "AMARILLO", 3, 40),
(5, "CHASE", "BLANCO CON CAFE",2, 4),
(6, "SOLOVINO", "NEGRO", 4, 8);

SELECT * FROM PERROS;

/*
		CASE SIMPLE
        
        CASE expresion
				WHEN valor 1 THEN resultado 1
                WHEN valor 2 THEN resultado 2
                ........
                ELSE resultado_predeterminado
			END
					
*/

SELECT NOMBRE, COLOR,
(
	CASE RAZA
		WHEN 1 THEN "PASTOR BELGA"
        WHEN 2 THEN "CHIHUAHUA"
        WHEN 3 THEN "BOXER"
        ELSE "MESTIZO"
	END
) AS RAZA, CONCAT(PESO, "kg") AS PESO,
(
	CASE 
		WHEN PESO >= 20 THEN "ES UN PERRO GRANDE"
		WHEN PESO <=5 THEN "ES UN PERRO PEQUEÑO"
		ELSE "ES UN PERRO MEDIANO"
	END
) AS DESCRIPCION 
FROM PERROS;






















