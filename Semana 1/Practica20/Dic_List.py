#Una lista dentro de un diccionario
empleados = {
    "nombre": ["Juan", "Ana", "Pedro"],
    "dep": ["Ventas", "Marketing", "Finanzas"],
    "estado": ["CDMX", "Jalisco", "Nuevo Leon"],
    "puesto": ["Vendedor", "Analista", "Gerente"]
}

#Funcion para mostrar los empleados 
def mostrar_empleados():
    for i in range(len(empleados["nombre"])):
        print(f"Empleado {i + 1}:")
        print(f"Nombre: {empleados['nombre'][i]}")
        print(f"Departamento: {empleados['dep'][i]}")
        print(f"Estado: {empleados['estado'][i]}")
        print(f"Puesto: {empleados['puesto'][i]}")
        print("-" * 20)

#Guardar un empleado
def guardar_empleado(nombre, departamento, estado, puesto):
    empleados["nombre"].append(nombre)
    empleados["dep"].append(departamento)
    empleados["estado"].append(estado)
    empleados["puesto"].append(puesto)
    print(f"\nEmpleado {nombre} guardado correctamente.")

#Funcion para editar 
def editar_empleado(indice, nombre = None, departamento = None, estado = None, puesto = None):
    if 0 <= indice < len(empleados["nombre"]):
        if nombre: empleados["nombre"][indice] = nombre
        if departamento: empleados["dep"][indice] = departamento
        if estado: empleados["estado"][indice] = estado
        if puesto: empleados["puesto"][indice] = puesto
        print(f"\nEl empleado {empleados["nombre"][indice]} se edito correctamente")
    else:
        print("Indice de empleado no valido")

#Funcion para elimiar empleado
def eliminar_empleado(indice):
    if 0 <= indice < len(empleados["nombre"]):
        nombre_eliminado = empleados["nombre"].pop(indice)
        empleados["dep"].pop(indice)
        empleados["estado"].pop(indice)
        empleados["puesto"].pop(indice)
        print(f"\nEl empleado {nombre_eliminado} se elimino correctamente")
    else:
        print("Indice de empleado no valido")

#Funcion para buscar el empleado
def buscar_emeplado(nombre_buscar):
    for i in range(len(empleados["nombre"])):
        if empleados["nombre"][i].lower() == nombre_buscar.lower():
            print(f"\nEmpleado Encontrado: ")
            print(f"\tNombre {empleados['nombre'][i]}")
            print(f"\tDepartamento {empleados['dep'][i]}")
            print(f"\tEstado {empleados['estado'][i]}")
            print(f"\tPuesto {empleados['puesto'][i]}")
            print("-" * 40)
            return
    print(f"Empleado {nombre_buscar} no encontrado.")

mostrar_empleados()

guardar_empleado("Pedro", "TI", "Veracruz", "Jefe")
mostrar_empleados()

editar_empleado(0, "Juan Perez", "RH", "Guadalajara", "JEFE")
mostrar_empleados()

eliminar_empleado(1)
mostrar_empleados()

buscar_emeplado("Juan Perez")

class

