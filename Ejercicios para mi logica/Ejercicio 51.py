"""
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos 
de cada asignatura en el formato <asignatura> tiene <créditos> créditos, 
donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. 
Al final debe mostrar también el número total de créditos del curso.
"""
def asignar_creditos(dic_materias):
    for materia in dic_materias.keys():
        creditos = int(input(f"Ingrese los créditos para {materia}: "))
        dic_materias[materia] = creditos
        suma = sum(dic_materias.values())

    print(f"\nCréditos asignados a las materias:{dic_materias}")
    print(f"\nLa suma total de créditos asignados es: {suma}\n")
        
    

while True:

    dic_materias = {
    "Matemáticas": 0,
    "Física": 0,
    "Química": 0,
    "Historia": 0,
    "Lengua": 0
} 
    try:
        print("\nBIENVENIDO AL PROGRAMA DE ASIGNACIÓN DE CRÉDITOS")
        opcion = input("¿Deseas asignar creditos a las materias?(si/no): ").lower()

        if opcion == "no":
            print("Gracias por usar el programa")
            break
        elif opcion == "si":
            asignar_creditos(dic_materias)
            print("Créditos asignados correctamente:")
    except ValueError:
        print("Error: Debes ingresar un número entero para los créditos.")