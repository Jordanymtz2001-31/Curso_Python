def gurdar_datos(nombre, direccion, edad, telefono):
    diccionario = {
        "Nombre": nombre,
        "Direccion": direccion,
        "Edad": edad,
        "Telefono": telefono}
    return f"Su nombre es {diccionario['Nombre']}, su direccion es {diccionario['Direccion']}, su edad es {diccionario['Edad']} y su telefono es {diccionario['Telefono']}"

while True:
    res = input("Ingresa los datos o exit para salir: ").lower()
    if res != "exit":
        nombre = input("Ingrese su nombre: ")
        direccion = input("Ingresa tu direccion: ")
        edad = int(input("Ingresa tu edad: "))
        telefono = int(input("Ingresa tu telefono: "))
        print(gurdar_datos(nombre, direccion, edad, telefono))
    else:
        print("Gracias por usar el programa")
        break

