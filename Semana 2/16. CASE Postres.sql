CREATE TABLE POSTRES(
	ID_POSTRE INT PRIMARY KEY,
    TIPO VARCHAR(25),
    PRECIO INT
);

INSERT INTO POSTRES VALUES
						(1, "PAY DE LIMON", 150),
                        (2, "PASTEL", 300), 
                        (3, "GELATINA", 100),
                        (4, "CUPCAKE", 50),
                        (5, "FLAN", 200),
                        (6, "CARLOTA", 80);
                        
SELECT * FROM POSTRES;

SELECT TIPO, CONCAT("$", FORMAT(PRECIO,2), "PRECIO MX") AS PRECIO, 
(
	CASE 
		WHEN PRECIO >= 200 THEN "ES UN POSTRE CARO"
        WHEN PRECIO <= 100 THEN "ES UN POSTRE BARATO"
        ELSE "ES UN POSTRE DE BUEN PRECIO"
	END
) AS MENSAJE
FROM POSTRES;
                        