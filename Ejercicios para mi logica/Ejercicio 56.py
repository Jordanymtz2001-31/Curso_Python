"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje 
de IVA, deberá aplicar un 21%.
"""

# Aqui creamos la funcion para calcular el total con IVA, ya sea que ingresan o no el iva
def total_con_iva(precio_unitario, cantidad, iva = 0.21):
    subtotal = precio_unitario * cantidad
    total_iva = subtotal * iva
    return subtotal + total_iva


while True:
    print("\nBIENVENIDO AL PROGRAMA DE FACTURAS")
    # Capturamos errores generales
    try:
        res = str(input("¿Desea con factura ? (si/no): ")).lower()
        if res == "no":
            print("Gracias por usar el programa")
            break
        # Validamos que la respuesta sea correcta
        elif res != "si" and res != "no":
            print("Respuesta no valida. Por favor ingrese 'si' o 'no'.\n")
        elif res == "si":
            precio_unitario = float(input("Ingrese el precio sin IVA: "))
            cant = int(input("Ingrese la cantidad de productos: "))
            iva_input = str(input("Desea ingresar el IVA (por ejemplo 0.21 para 21%) o precione enter para usar el 21%: ")).strip() # strip para eliminar espacios en blanco
            # Si el usuario no ingresa nada, se usa el valor por defecto del 21%
            iva = float(iva_input) if iva_input else 0.21

            # Calculamos el total con IVA con la funcion creada
            total = total_con_iva(precio_unitario, cant, iva)        
            print(f"El total de la factura es: {total:.2f}\n")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese números correctos para precio, cantidad e IVA.\n")
            

