materias = ["Matemáticas", "Física", "Química", "Historia",  "Lengua"]

def eliminar_materia_aprobada(materias):
    calificaciones = {}
    for m in materias:
        calificacion = input(f"Dame la calificacion de {m}:")
        # Convertir la calificación a entero y almacenarla en el diccionario    
        calificaciones[m] = int(calificacion)
    # Eliminar las materias aprobadas (calificación >= 6)
    for m in list(calificaciones.keys()):
        if calificaciones[m] >= 60:
            del calificaciones[m]
    return f"las calificaciones reprobadas son: {calificaciones}"

print(eliminar_materia_aprobada(materias))