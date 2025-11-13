estudiantes = [
    {"nombre": "Juan", "edad": 20, "nota": [85, 90, 78]},
    {"nombre": "Ana", "edad": 22, "nota": [88.5, 92, 80]},
    {"nombre": "Luis", "edad": 21, "nota": [75, 80.5, 70]},
    {"nombre": "Maria", "edad": 23, "nota": [90, 95, 88.5]}
]

calcular_promedio = lambda calificaciones: sum(calificaciones) / len(calificaciones)

for estudiante in estudiantes:
    promedio = calcular_promedio(estudiante["nota"])
    print(f"El promedio de {estudiante['nombre']} es: {promedio:.2f}")

#Agregamos la clave promedio al diccionario
for estudiante in estudiantes:
    estudiante["promedio"] = calcular_promedio(estudiante["nota"])

#Listamos los estudiantes con su promedio
print("\nLista de estudiantes con su promedio:")
for estudiante in estudiantes:
    print(f"{estudiante['nombre']}: {estudiante['promedio']:.2f}")

#filtramos los estudiantes con promedio mayor a 80
estudiantes_aprobados = list(filter(lambda est: est["promedio"] > 80, estudiantes))
print("\nEstudiantes con promedio mayor a 80:")
for estudiante in estudiantes_aprobados:
    print(f"{estudiante['nombre']}: {estudiante['promedio']:.2f}")

#ordenamos por promedio de mayor a menor
ordenados_por_promedio = sorted(estudiantes, key=lambda est: est["promedio"], reverse=True)
print("\nEstudiantes ordenados por promedio (de mayor a menor):")
for estudiante in ordenados_por_promedio:
    print(f"{estudiante['nombre']}: {estudiante['promedio']:.2f}")