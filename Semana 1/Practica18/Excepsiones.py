try:
    nombre = input("Introduce tu nombre: ")
    if len(nombre) > 1:
        nombre_usuario = "El nombre es: " + nombre
    print(nombre_usuario)
except:
    print("\nHa ocurrido un error")
else:
    print("\nSalimos correctamente")
finally:
    print("\nEl bloque finally se ejecuta siempre")