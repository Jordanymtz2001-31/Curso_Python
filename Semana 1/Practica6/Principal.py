from Productos import Productos
from Perecedero import Perecedero
from Noperecedero import Noperecedero

def main():

    #Creamos una lista y ahi mismos metemos los objetos
    productos = [
        Productos("Gel", 40.00),
        Perecedero("Leche", 20.00, 2),
        Noperecedero("Jabon", 15.00, "Higiene")
    ]

    #Mostrar los productos

    #Creamos una variables total 
    total = 0

    print("-----Lista de productos-----")
    for producto in productos:
        precio = producto.calcular(2) #Calculamos el precio de cada producto
        total += precio #Sumamos el precio al total
        print(f"El precio de {producto.nombre} es: ${precio:.2f}")

    print(f"\nEl total de la compra es: {total:.2f}")

if __name__ == "__main__":
    main()