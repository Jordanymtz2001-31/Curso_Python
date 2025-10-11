try:
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))

    try:
        edad = int(edad)
    except ValueError:
        raise ValueError("La edad debe ser un número entero.")
    
    if edad < 1 or edad > 120:
        raise ValueError("La edad debe estar entre 1 y 120.")
    elif len(nombre) <= 3:
        raise ValueError("El nombre debe tener al menos 3 caracteres.")
    else:
        print(f"Hola {nombre}, tienes {edad} años.")

except ValueError as ve: #El ve es el alias del error y se puede llamar como se quiera
    print(f"Error: {ve}\n Introduce los datos correctamente.")
    