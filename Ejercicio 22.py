edad = int(input("Dame tu edad: "))

def categoria_edad(edad):
    if not edad:
        return "No se ingreso nungun valor"
    elif edad < 4:
        return "Entrada gratuita"
    elif edad in range(4, 18):
        return "Precio de la entrada: $10"
    elif edad in range(18, 65):
        return "Precio de la entrada: $20"
    else:
        return "Dato no valido"
    
print(categoria_edad(edad))