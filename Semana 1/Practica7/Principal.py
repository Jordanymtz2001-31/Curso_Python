from Persona import Persona
from Estudiante import Estudiante
from Curso import Curso

# Función principal
def main():

    # Crear instancias de curso
    curso1 = Curso("Matemáticas")
    curso2 = Curso("Física")

    # Crear instancias de estudiantes
    estudiante1 = Estudiante("Jordany", 24, "A001")
    estudiante2 = Estudiante("Ana", 22, "A002")
    estudiante3 = Estudiante("Luis", 23, "A003")

    # Agregar estudiantes al curso
    curso1.agregar_estudiantes(estudiante1)
    curso1.agregar_estudiantes(estudiante2) 
    curso2.agregar_estudiantes(estudiante3)

    #Creamos una lista de los cursos
    cursos = [curso1, curso2]

    #Creamos el menu
    while True:
        print("\n--- Menu principal---")
        print("1.- Crear un nuevo curso")
        print("2.- Ver cursos")
        print("3.- Agregar estudiante a un curso")
        print("4.- Eliminar estudiante de un curso")
        print("5.- Ver estudiantes de un curso")
        print("6.- Eliminar un curso")
        print("7.- Salir")

        opcion = input("Seleccione una opción (1-7): ")

        match opcion:
            case "1":
                nombre_curso = input("Ingrese el nombre del nuevo curso: ")
                nuevo_curso = Curso(nombre_curso)
                cursos.append(nuevo_curso) # Agregamos a la lista de cursos
                print(f"Curso '{nombre_curso}' creado exitosamente.")
            
            case "2":
                if not cursos:
                    print("No hay cursos disponibles.")
                else:
                    for i, curs in enumerate(cursos, start=1):
                        print(f"{i + 1}. {curs.nombre}")

            case "3":
                if not cursos:
                    print("No hay cursos disponibles para agregar estudiantes.")
                    continue
                #Con el for mostramos los cursos
                #El for funciona para buscar el indice y el objeto
                for i, curs in enumerate(cursos, start=1): #el i es el indice y curs es el objeto
                    print(f"{i}. {curs.nombre}")

                indice_curso = int(input("Seleccione el número del curso al que desea agregar un estudiante: ")) - 1

                nombre = input("Nombre del estudiante: ")
                edad = int(input("Edad del estudiante: "))
                matricula = input("Matrícula del estudiante: ")

                new_estudiante = Estudiante(nombre, edad, matricula)

                #Agregar el estudiante al curso seleccionado
                cursos[indice_curso].agregar_estudiantes(new_estudiante)
                print(f"Estudiante '{nombre}' agregado al curso '{cursos[indice_curso].nombre}' exitosamente.")

            case "4":
                if not cursos:
                    print("No hay cursos disponibles para eliminar estudiantes.")
                    continue    
                for i, curs in enumerate(cursos, start=1):
                    print(f"{i}. {curs.nombre}")

                indice_curso = int(input("Seleccione el indice del curso ")) - 1

                print("\nEstudiantes en {cursos[indice_curso].nombre}: ")
                cursos[indice_curso].listar_estudiantes() #Mostramos los estudiantes del curso

                matricula = input("Ingrese la matrícula del estudiante que desea eliminar: ")

                if cursos[indice_curso].eliminar_estudiantes(matricula):
                    print(f"Estudiante con matrícula '{matricula}' eliminado del curso '{cursos[indice_curso].nombre}' exitosamente.")
                else:
                    print(f"No se encontró un estudiante con matrícula '{matricula}' en el curso '{cursos[indice_curso].nombre}'.")

            case "5":
                if not cursos:
                    print("No hay cursos disponibles para ver estudiantes.")
                    continue

                for i, curs in enumerate(cursos, start=1):
                    print(f"{i}. {curs.nombre}")

                indice_curso = int(input("Seleccione el número del curso para ver sus estudiantes: ")) - 1
                
                print(f"\nEstudiantes en el curso '{cursos[indice_curso].nombre}':") #Mostramos el nombre del curso
                cursos[indice_curso].listar_estudiantes() #Mostramos los estudiantes del curso

            case "6":
                if not cursos:
                    print("No hay cursos disponibles para eliminar.")
                    continue

                for i, curs in enumerate(cursos, start=1):
                    print(f"{i}. {curs.nombre}")

                indice_curso = int(input("Seleccione el número del curso que desea eliminar: ")) - 1
                curso_eliminado = cursos.pop(indice_curso) #Elimina el curso de la lista    
                print(f"Curso '{curso_eliminado.nombre}' eliminado exitosamente.")
            
            case "7":
                print("Saliendo del programa....")
                break

            case _:
                print("Opción inválida, intente de nuevo.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()  