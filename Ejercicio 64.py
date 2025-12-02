"""
Escribir una función que aplique un descuento a un precio y 
otra que aplique el IVA a un precio
"""
# Funcion de descuento si pasa de 500
def decuento(precio, cantidad):
    total = precio * cantidad
    if total > 500:
        descuento = total * 0.20
        total = total - descuento
        return total
    else:
        return total
    
# Funcion de el total mas el iva
def precio_iva(descuento, iva=0.20):
    iva = descuento * iva
    total = descuento + iva
    return total

while True:
    try:
        print("SISTEMA DE COMPRAS")
        res = input("Deseas comprar (si/no): ").lower()

        if res == "":
            print("Debes de colocar si o no")
        elif res == "no":
            print("Gracias por ver mis sistema")
            break
        elif res == "si":
            producto = input("Dime el nombre del producto: ")
            precio = float(input("Damel el precio unitario: "))
            cantidad = int(input("¿Cuantos va a llevar?: "))
            descuento = decuento(precio, cantidad)
            print(f"El precio con descuento es ${decuento(precio, cantidad)}")
            print(f"El precio con descueto y el iva es de {precio_iva(descuento)}\n")
    except TypeError:
        print("Erro debes de colocar los datos correctos")
    except Exception as e:
        print("Error: ocurrio un error en {e}")
