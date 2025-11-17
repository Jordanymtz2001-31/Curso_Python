curso = ["Matematicas", "Fisica", "Quimica", "Historia"]

def notas_curso(curso):
    notas = []
    for materia in curso:
        nota = input(f"Ingresa la nota de {materia}: ")
        notas.append(nota)
    for materia in range(len(curso)):
        print(f"\nEn {curso[materia]} has sacado {notas[materia]}")

notas_curso(curso)