
edad = int(input("Ingresa tu edad: "))

def conteo_edad(edad):
    if edad == "":
        return "No se ingreso ninguna edad"
    elif edad < 0:
        return "La edad no puede ser negativa"
    else:
        mensajes = []
        for año in range(edad + 1):
            mensajes.append(f"Has cumplido {año} años") #Se agrega el mensaje a la lista
        return "\n".join(mensajes) # Se unen los mensajes con saltos de línea
    # Esto se hace por que se usa menos memoria que imprimir directamente en el ciclo
    # y es mas eficiente para edades grandes
    
print(conteo_edad(edad))