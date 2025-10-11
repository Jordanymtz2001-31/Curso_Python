from Persona_Abstr import Persona
from Estudiante import Estudiante
from Profesor import Profesor
from Materia import Materia
from Escuela import Escuela

    
def main():
    
    #Creamos el objeto estudiantes
    estudiante1 = Estudiante("01A", "Juan", 22)
    estudiante2 = Estudiante("02B", "Maria", 21)
    estudiante3 = Estudiante("03C", "Pedro", 23)
    estudiante4 = Estudiante("04D", "Ana", 20)
    estudiante5 = Estudiante("05E", "Luis", 24)
    estudiante6 = Estudiante("06F", "Sofia", 22)
    estudiante7 = Estudiante("07G", "Carlos", 21)
    estudiante8 = Estudiante("08H", "Laura", 23)
    estudiante9 = Estudiante("09I", "Javier", 20)
    estudiante10 = Estudiante("10J", "Diego", 22)

    #Creamos el objeto profesor
    profe1 = Profesor("001", "Dr. Smith", 25, "Matematicas")
    profe2 = Profesor("002", "Dr. Ana", 30, "Calculo")

    #Creamos el objeto Materias
    materia1 = Materia("Matematicas", profe1)
    materia2 = Materia("Calculo", profe1)
    materia3 = Materia("Fisica", profe2)
    materia4 = Materia("Quimica", profe2)
    materia5 = Materia("Biologia", profe2)

    #Creamos el objeto para la escuela
    escuela = Escuela()

    #Agregamos los profesores a la escuela
    escuela.lista_profesores.append(profe1)
    escuela.lista_profesores.append(profe2)

    #Agregamos todas las materias a la escuela
    escuela.lista_materias.append(materia1)
    escuela.lista_materias.append(materia2)
    escuela.lista_materias.append(materia3)
    escuela.lista_materias.append(materia4)
    escuela.lista_materias.append(materia5)


    #Agregamos estudiantes a la esuela
    escuela.lista_estudiantes.extend([
        estudiante1, estudiante2, estudiante3, estudiante4, estudiante5,
        estudiante6, estudiante7, estudiante8, estudiante9, estudiante10
    ])

    #Agregar algunas calificaciones
    estudiante1.agregar_calificacion("Matematicas", 80)
    estudiante2.agregar_calificacion("Fisica", 70)
    estudiante1.agregar_calificacion("Ingles", 89)
    estudiante3.agregar_calificacion("Matematicas", 70)
    estudiante4.agregar_calificacion("Quimica", 40)
    estudiante5.agregar_calificacion("Español", 85)

    # Matemáticas
    materia1.agregar_estudiante(estudiante1)  # Juan - 80
    materia1.agregar_estudiante(estudiante3)  # Pedro - 70  
    materia1.agregar_estudiante(estudiante5)  # Luis
    estudiante5.agregar_calificacion("Matematicas", 95)

    # Cálculo
    materia2.agregar_estudiante(estudiante6)  # Sofia
    estudiante6.agregar_calificacion("Calculo", 45)  # REPROBADO
    materia2.agregar_estudiante(estudiante7)  # Carlos
    estudiante7.agregar_calificacion("Calculo", 78)

    # Física
    materia3.agregar_estudiante(estudiante2)  # Maria - 70
    materia3.agregar_estudiante(estudiante8)  # Laura
    estudiante8.agregar_calificacion("Fisica", 92)

    # Química
    materia4.agregar_estudiante(estudiante4)  # Ana - 40 REPROBADO
    materia4.agregar_estudiante(estudiante9)  # Javier
    estudiante9.agregar_calificacion("Quimica", 85)

    # Biología
    materia5.agregar_estudiante(estudiante10)  # Juan
    estudiante10.agregar_calificacion("Biologia", 55)  # REPROBADO

    while True:
        print("\n-----GESTION ACADEMICA-----")
        print("1.- Agregar estudiante")
        print("2.- Agregar profesor")
        print("3.- Agregar materia")
        print("4.- Agregar calificaciones a estudiantes")
        print("5.- Mostrar lista de estudiantes")
        print("6.- Mostrar Profesores")
        print("7.- Lista de Materias")
        print("8.- Lista de Alumnos Aprobados")
        print("9.- Lista de Alumnos Reprobados")
        print("10.- Agregar Estudiantes a materia")
        print("11.- Ver calificaciones de un estudiantes mediante su matricula")
        print("12.- Salir")

        try:

            opcion = input("Seleciona una opcion(1-12): ")
            if not opcion.isdigit() or not (1 <= int(opcion) <= 12):
                raise ValueError("Opcion debe ser un numero entre 1 y 12")
        except ValueError as e:
            print(f"Error: {e}")
            continue

        match opcion:
            case "1":
                escuela.agregar_estudiante()
            case "2":
                escuela.agregar_profesor()
            case "3":
                escuela.agregar_materia()
            case "4":
                escuela.agregar_calificacion_estudiante()
            case "5":
                escuela.mostrar_estudiantes()
            case "6":
                escuela.mostrar_profesores()
            case "7":
                escuela.mostrar_materias()
            case "8":
                escuela.mostrar_estudiantes_aprobados()
            case "9":
                escuela.mostrar_estudiantes_reprobados()
            case "10":
                escuela.agregar_estudiante_a_materia()
            case "11":
                escuela.ver_calificaciones_estudiante()
            case "12":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida")


if __name__ == "__main__":
    main()