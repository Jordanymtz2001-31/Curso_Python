"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de 
ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje 
informando de ello.
"""
frutas = {"Platano" : 1.35, "Manzana" : 0.80, "Pera" : 0.85, "Naranja" : 0.70}

while True:
    print("BIENVENIDO A LA TIENDA DE FRUTAS")
    res = input("¿Quieres comprar alguna fruta? (si/no)").lower()

    if res == "no":
        print("Gracias por su visita")
        break
    elif res == "si":
        fruta = input("Ingrese la fruta que desea comprar: ").lower().capitalize() #El capitalize es para que la primera letra sea mayuscula y las demas minusculas
        if fruta in frutas:
            cantidad = int(input(f"¿Cuantos piezas quieres?"))
            precio_total = cantidad * frutas[fruta]
            print(f"El precio total es de: {precio_total:.2f} pesos")
        else:
            print(f"Lo siento, no tenemos esa fruta disponible.")


