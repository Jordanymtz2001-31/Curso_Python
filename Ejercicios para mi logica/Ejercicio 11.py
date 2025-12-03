fecha = input("Ingrese la fecha de nacimiento en formato dd/mm/aaaa: ")

# Mostrar la el dia, mes y año
def separar_fecha(fecha):
    # Se paramos las fechas con el separador "/"
    dia, mes, anio = fecha.split("/")
    return f"Dia: {dia}, Mes: {mes}, Año: {anio}"