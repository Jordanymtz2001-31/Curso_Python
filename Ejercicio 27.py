num = int(input("Dame un numero: "))

def desendente(num):
    if num < 0:
        return "El numero no puede ser negativo"
    elif num == "":
        return "No se ingreso ningun numero"
    else:
        mensaje = []
        # El primer -1 es el valor final (no incluido)
        # El segundo -1 es el paso para desender (decremento)
        for num in range(num, -1, -1):
            mensaje.append(num)

    return mensaje

print(desendente(num))