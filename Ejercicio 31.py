CONTRASEAS_VALIDAS = "Dany12345"

def verificar_contraseña(contraseña):
    
    if contraseña == "":
        return "No se ingreso ninguna contrseña"
    elif contraseña == CONTRASEAS_VALIDAS:
        return "Contraseña correcta"
    else:
        return "Contraseña incorrecta"
    
contraseña = input("Introduce una contraseña: ")

# Bucle hasta que la contraseña sea correcta
while verificar_contraseña(contraseña) != "Contraseña correcta":
    # Imprime el resultado de la verificación
    print(verificar_contraseña(contraseña))
    # Sigue pidiendo la contraseña
    contraseña = input("Vuelve a introducir una contraseña: ")