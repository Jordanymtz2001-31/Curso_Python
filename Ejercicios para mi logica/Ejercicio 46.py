"""
Escribir un programa que pregunte por una muestra de números, separados por comas, 
los guarde en una lista y muestre por pantalla su media y desviación típica.
"""


numeros = input("Ingrese una muestra de números separados por comas: ")

def calcular_media_desviacion(numeros):
    # Convertir la cadena de números en una lista de flotantes
    lista_numeros = [float(num) for num in numeros.split(",")]
    
    media = sum(lista_numeros) / len(lista_numeros)
    desviacion = (sum((x - media) ** 2 for x in lista_numeros) / len(lista_numeros)) ** 0.5
    return f"La media es {media} y la desviación típica es {desviacion}"

print(calcular_media_desviacion(numeros))