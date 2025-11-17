"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
"""

facturas = {}
cobrado = 0
pendiente = 0
opcion = ""

while opcion != "T":
    print("\nBIENVENIDO AL SISTEMA DE FACTURAS")
    opcion = input("Quieres crear una nueva facruta (F), pagarla (P), terminar(T): ")

    if opcion == "T":
        print("Gracias por nada")
        break
    elif opcion == "F":
        clave = input("Dame el numero de la factura: ")
        coste = float(input("Dame el coste de la factura: ")) 
        facturas[clave] = coste
        pendiente += coste
    elif opcion == "P":
        clave = input("Introduce la factura a pagar: ")
        coste = facturas.pop(clave, 0)
        cobrado += coste
        pendiente -= coste

    print("Recaudado: ", cobrado)
    print("Pendiente de cobro: ", pendiente)
    

        