def factorial(num):
    res = 1
    for m in range(1, num + 1):
        res *= m
    return res

while True:
    try:
        print("\nHOLA A MI PROGRAMA")
        opcion = input("Dime si quieres usar mi programa(si/no): ")
        if opcion == "no":
            print("Gracias por intentarlo")
            break
        elif opcion == "si":
            num = int(input("Dame el numero: "))
            print(f"El factorial de {num} es {factorial(num)}")
    except Exception as e:
        print(f"Error: {e}. Coloca el dato correcto.")