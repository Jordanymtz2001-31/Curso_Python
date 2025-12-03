"""
Escribir un programa que cree un diccionario simulando una cesta de la compra. 
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
hasta que el usuario decida terminar. Después se debe mostrar por pantalla la 
lista de la compra y el coste total, con el siguiente formato
"""

def carrito(dic_productos):
    total = sum(dic_productos.values())
    return f"Los productos son {dic_productos} y el total {total} pesos"

dic_productos = {}

while True:
    print("\BIENVENIDOS A CARRITO")
    opcion = input("¿Deseas comprar?(si/no): ").lower()
    if opcion == "no":
        print("Gracias por usar el programa")
        break
    elif opcion == "si":
        clave = input("Dime el producto: ")
        valor = float(input("Dime el precio: "))
        dic_productos[clave] = valor
        print (carrito(dic_productos))
