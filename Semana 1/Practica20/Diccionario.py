#Creamos un diccionario
diccionario = {"nombre": "Juan",
               "edad": 30,
               "ciudad": "Madrid"}

print(diccionario)

#Aceder a un valor
print(diccionario["nombre"]) #Juan
print(diccionario.get("edad")) #30

#Agregar un nuevo par clave-valor
diccionario["profesion"] = "Ingeniero"


#Modificar un valor existente
diccionario["edad"] = 31

#Eliminar un par clave-valor
del diccionario["ciudad"]

#Ejemplo 2 
diccionario2 = {"Juan" : [25, 1.50], "Ana" : [30, 1.60], "Luis" : [28, 1.80]}
print(diccionario2)

#Accedemos solo a la edad de Ana
print(diccionario2["Ana"][0]) #30

#Ejmplo 3 subdiccionarios
diccionario3 = {
    "Empleado1": {"Nombre": "Carlos", "Edad": 28, "Departamento": "Ventas"},
    "Empleado2": {"Nombre": "Ana", "Edad": 32, "Departamento": "Marketing"}
}

print(diccionario3)

#Accedemos a la edad de Ana
print(diccionario3["Empleado2"]["Edad"]) #32
print("La estatura de Luis es:", diccionario2["Luis"][1]) #1.80

#Ejemplo 4
empleados = {1 : "Karen", 2 : "Luis", 3 : "Ana"}
print(empleados)

#Mostrar 1 empleado
print(empleados[2]) #Luis

#Agregar un empleado
empleados[4] = "Pedro"

#Si no existe la clave, no hace nada
empleados.get(5, "No existe el empleado") #No existe el empleado    

#Existe la clave
print(1 in empleados) #True 
print(5 in empleados) #False

#Imprimir todas las claves
print(empleados.keys())

#Imprimir todos los valores
print(empleados.values())