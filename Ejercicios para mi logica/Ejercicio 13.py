"""
Escribir un programa que pregunte el nombre el un producto, su precio 
y un número de unidades y muestre por pantalla una cadena con el nombre 
del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, 
el número de unidades con tres dígitos y el coste total con 8 dígitos enteros 
y 2 decimales.
"""

nombre_producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
unidades = int(input("Ingrese el numero de unidades: "))

def mostrar_informacion_producto(nombre_producto, precio, unidades):
    costo_total = precio * unidades
    return (f"Producto: {nombre_producto}, "
            f"Precio Unitario: {precio:9.2f}, "
            f"Unidades: {unidades:3d}, "
            f"Costo Total: {costo_total:8.2f}")

print(mostrar_informacion_producto(nombre_producto, precio, unidades))