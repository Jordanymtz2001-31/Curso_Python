class Curso:

    def __init__(self, nombre):
        self.nombre = nombre
        self.profesores = None #Agregacion
        self.estudiantes = [] #Agregacion

    #Metodos para agregar profesores y estudiantes
    def agregar_profesores(self, profesores):
        self.profesores = profesores

    def agregar_estudiantes(self, estudiantes):
        self.estudiantes.append(estudiantes)

    #Metodo para mostrar la informacion del curso
    def mostrar_info(self):
        print(f"\nCurso: {self.nombre}")
        if self.profesores:
            print(f"Profesor: {self.profesores}")
        else:
            print("No hay profesor asignado.")

        print("\nEstudiantes inscritos:")
        if self.estudiantes:
            for estudiante in self.estudiantes:
                print(f"- {estudiante}")
        else:
            print("No hay estudiantes asignados.")