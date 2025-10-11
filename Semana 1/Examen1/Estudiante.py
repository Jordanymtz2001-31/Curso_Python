#Clase Estudiante que ereda de Persona
from Persona_Abstr import Persona

class Estudiante(Persona):
    def __init__(self, matricula, nombre, edad, calificaciones = None):
        super().__init__(matricula,nombre, edad)
        self.calificaciones = calificaciones if calificaciones is not None else {}

    #Metodo para agregar calificaciones
    def agregar_calificacion(self, materia, calificacion):
        try : #isinstances es para verificar el tipo de dato
            if not isinstance(materia, str) or not materia.strip():
                raise ValueError("La materia debe ser una cadena no vacía.")
            
            if not isinstance(calificacion, (int, float)):
                raise TypeError("La calificacion debe de ser numero")
            
            if not (0 <= calificacion <=100):
                raise ValueError("La calificion debe ser entre 1 y 100")

            #Aqui se agrega la calificacion a la materia correspondiente
            # Se utiliza title() para estandarizar el nombre de la materia
            # round() para redondear la calificacion a 2 decimales
            self.calificaciones[materia.strip().title()] = round(float(calificacion),2)
            print(f"Calificacion agregada: {materia} = {calificacion}")

        except (ValueError, TypeError) as e:
            print(f"Error al agregar Calificacion: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    #Metodo para calcular el promedio de calificaciones
    def calcular_promedio(self):
        try:
            # Si no hay calificaciones devolvemos 0 (no lanzar/retornar un ValueError)
            if not self.calificaciones:
                return 0
            
            total = sum(self.calificaciones.values()) # Suma todas las calificaciones
            promedio = total / len(self.calificaciones)   # Retorna el promedio
            return round(promedio, 2)

        except Exception as e:
            # Registrar el error y devolver 0 como fallback seguro
            print(f"Error al calcular promedio para {getattr(self, 'nombre', 'Alumno')}: {e}")
            return 0
        
    #Implementacion del metodo abstracto
    def mostrar_datos(self):
        print(f"El alumno: {self.nombre} con Promedio de: {self.calcular_promedio()}\n")