dic = {'Maria': 80, 'Mario': 90, 'Yen': 53}

def reprobados(dic):
    for estudiante, calificacion in dic.items():
        if calificacion < 60 :
            reprobados = estudiante
    return f"Los reprobados son {reprobados} con {calificacion} de calificación"

print(reprobados(dic))



