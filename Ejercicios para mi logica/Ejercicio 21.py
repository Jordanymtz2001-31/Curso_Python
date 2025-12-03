inalcanzable = 0.0
aceptable = 0.4
meritoria = 0.6

nivel = 2400

desempeño = input("Ingrese el desempeño del empleado (inalcanzable, aceptable, meritoria): ").strip().lower()

def calcular_aumento(desempeño):
    if desempeño == "":
        return "No se ingreso nungun valor"
    elif desempeño == "inalcanzable":
        return "El aumento es del 0%"
    elif desempeño == "aceptable":
        return f"El aumento es del 4%, es decir ${aceptable * nivel} es el aumento"
    elif desempeño == "meritoria":
        return f"El aumento es del 6%, es decir ${meritoria * nivel} es el aumento"
    else:
        return "Desempeño no reconocido"
    
print(calcular_aumento(desempeño))