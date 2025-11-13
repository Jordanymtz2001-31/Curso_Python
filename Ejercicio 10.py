"""
Escribir un programa que pregunte por consola el precio de un producto 
en pesos con dos decimales y muestre por pantalla el número de pesos 
y el número de céntimos del precio introducido.
"""

precio = float(input("Dame el precio del producto (con 2 decimales): "))


def separar_precio(precio):
    pesos = int(precio) # Pasamos el precio a entero para sacar los pesos
    centimos = precio - pesos #Sacamos los centimos
    centimos = round(centimos * 100) # Multiplicamos por 100 y redondeamos para obtener los centimos
    return f"El precio tiene {pesos} pesos y {centimos} centimos"

print(separar_precio(precio))
