"""
Escribir un programa que pregunte por consola por los productos de 
una cesta de la compra, separados por comas, y muestre por pantalla 
cada uno de los productos en una línea distinta.
"""

# Yo lo are aun mejor, con una lista y una funcion
productos = input("Ingrese los productos de la cesta de la compra: ")

lista_productos = productos.split(",")

def mostrar_productos(lista_productos):
    # Recorremos la lista por cada productos
    for producto in lista_productos:
        print(producto.strip()) # Usamos strip para eliminar espacios en blanco

print("Los productos de la lista son:")
mostrar_productos(lista_productos)
