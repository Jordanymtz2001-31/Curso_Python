from Persona import Persona
from Profesor import Profesor
from Estuadiante import Estudiante
from Cursos import Curso

# Crear personas
def main():

    #Instanciar personas
    persona1_profesor = Persona("Juan Perez", 40)
    persona2_profesor = Persona("Ana Gomez", 35)

    persona1_estudiante = Persona("Carlos Ruiz", 20)
    persona2_estudiante = Persona("Luisa Fernandez", 22)
    persona3_estudiante = Persona("Marta Sanchez", 19)
    persona4_estudiante = Persona("Diego Torres", 21)
    persona5_estudiante = Persona("Sofia Morales", 23)

    #Instanciar profesores

    persona1 = Persona(persona1_profesor, "Matematicas")
    persona2 = Persona(persona2_profesor, "Fisica")

    #Instanciar estudiantes
    estudiante1 = Estudiante(persona1_estudiante, "A001")
    estudiante2 = Estudiante(persona2_estudiante, "A002")
    estudiante3 = Estudiante(persona3_estudiante, "A003")
    estudiante4 = Estudiante(persona4_estudiante, "A004")
    estudiante5 = Estudiante(persona5_estudiante, "A005")

    #Crear curso
    curso1 = Curso("Ingenieria de Software")
    curso2 = Curso("Base de Datos")

    #Asignar profesores al curso
    curso1.agregar_profesores(persona1)
    curso2.agregar_profesores(persona2)

    #Asignar estudiantes al curso
    curso1.agregar_estudiantes(estudiante1)
    curso1.agregar_estudiantes(estudiante2)
    curso1.agregar_estudiantes(estudiante3)
    curso2.agregar_estudiantes(estudiante4)
    curso2.agregar_estudiantes(estudiante5)

    #Crear lista de cursos
    cursos = [curso1, curso2]

    while True:
        print("\n--- SISTEMA DE GESTOR DE CURSOS ---")
        print("1.- Crear Curso")
        print("2.- Asignar Profesor a Curso")
        print("3.- Inscribir Estudiante a Curso")
        print("4.- Mostrar Informacion de Cursos")
        print("5.- Listar profresores")
        print("6.- Listar estudiantes")
        print("7.- Listar cursos")
        print("8.- Salir")

        opcion = input("Seleccione una opcion (1-8): ")

        match opcion:
            case "1":
                nombre_curso = input("Ingrese el nombre del curso: ")
                nuevo_curso = Curso(nombre_curso)
                cursos.append(nuevo_curso)
                print(f"Curso '{nombre_curso}' creado exitosamente.")
            
            case "2":
                if not cursos:
                    print("No hay cursos disponibles. Cree un curso primero.")
                    continue

                print("Cursos disponibles:")
                for idx, curso in enumerate(cursos, start=1):
                    print(f"{idx}. - {curso.nombre}") #Mostrar solo el nombre del curso desde la clase Curso

                # Seleccionar curso
                curso_idx = int(input("Seleccione el curso por numero: ")) - 1

                #Pedir datos del profesor
                nombre_profesor = input("\nNombre del profesor: ")
                edad_profesor = int(input("Edad del profesor: "))
                especialidad_profesor = input("Especialidad del profesor: ")

                #Instanciar persona y profesor
                persona_profesor = Persona(nombre_profesor, edad_profesor)
                profesor = Profesor(persona_profesor, especialidad_profesor)

                #Aqui se asigna el profesor al curso usando el metodo de la clase Curso
                cursos[curso_idx].agregar_profesores(profesor)
                print(f"\nProfesor '{nombre_profesor}' asignado al curso '{cursos[curso_idx].nombre}' exitosamente.")
            
            case "3":
                if not cursos:
                    print("No hay cursos disponibles. Cree un curso primero.")
                    continue    
                print("Cursos disponibles:")
                for idx, curso in enumerate(cursos, start=1):
                    print(f"{idx}. - {curso.nombre}") #Mostrar solo el nombre del curso desde la clase Curso
                
                # Seleccionar curso
                curso_idx = int(input("Seleccione el curso por numero: ")) - 1

                #Pedir datos del estudiante
                nombre_estudiante = input("\nNombre del estudiante: ")
                edad_estudiante = int(input("Edad del estudiante: "))
                matricula_estudiante = input("Matricula del estudiante: ")

                #Instanciar persona y estudiante
                persona_estudiante = Persona(nombre_estudiante, edad_estudiante)
                estudiante = Estudiante(persona_estudiante, matricula_estudiante)

                #Aqui se asigna el estudiante al curso usando el metodo de la clase Curso
                cursos[curso_idx].agregar_estudiantes(estudiante)
                print(f"\nEstudiante '{nombre_estudiante}' inscrito en el curso '{cursos[curso_idx].nombre}' exitosamente.")

            case "4":
                if not cursos:
                    print("No hay cursos disponibles. Cree un curso primero.")
                    continue

                for curso in cursos:
                    curso.mostrar_info()
                    print("\n" + "-"*40)

            case "5":
                print("\n--- LISTA DE PROFESORES ---")

                #Expresion ternaria para listar profesores
                profesor = {curso.profesores for curso in cursos if curso.profesores }
                if not profesor:
                    print("No hay profesores disponibles.")
                    continue
                for prof in profesor:
                    print(f"\n- {prof}")

            case "6":
                print("\n--- LISTA DE ESTUDIANTES ---")

                todos_estudiantes = []
                for curso in cursos:
                    todos_estudiantes.extend(curso.estudiantes) #Extiende la lista con los estudiantes de cada curso
                if not todos_estudiantes:
                    print("No hay estudiantes disponibles.")
                    continue
                for est in todos_estudiantes:
                    print(f"- {est}")

            case "7":
                print("\n--- LISTA DE CURSOS ---")
                for num, curso in enumerate(cursos, start=1):
                    print(f"{num}. - {curso.nombre}") #Mostrar solo el nombre del curso desde la clase Curso
                if not cursos:
                    print("No hay cursos disponibles.")
                    continue
            
            case "8":
                print("Saliendo del sistema. ¡Hasta luego!")
                break

            case _:
                print("Opcion no valida. Intente de nuevo.")

if __name__ == "__main__":
    main()
