# Clase Escuela
from Estudiante import Estudiante
from Profesor import Profesor
from Materia import Materia
from Persona_Abstr import Persona


class Escuela:

    def __init__(self, lista_estudiantes=None, lista_profesores=None, lista_materias=None):
        # Inicializo las listas si no se proporcionan
        self.lista_estudiantes = lista_estudiantes if lista_estudiantes is not None else []
        self.lista_profesores = lista_profesores if lista_profesores is not None else []
        self.lista_materias = lista_materias if lista_materias is not None else []

    
    #Metodo para agregar estudiantes
    def agregar_estudiante(self):
        try:
            print("\n=== AGREGAR NUEVO ESTUDIANTE ===")

            # --- PEDIR Y VALIDAR MATRÍCULA ---
            matricula = input("Ingrese la matricula del estudiante: ").strip()
            if not matricula:
                raise ValueError("La matrícula no puede estar vacía.")
            if not Estudiante.validar_matricula(matricula):
                raise ValueError("Matrícula inválida. Debe ser alfanumérica.")
            if any(est.matricula == matricula for est in self.lista_estudiantes):
                raise ValueError(f"Ya existe un estudiante con la matrícula {matricula}")
            
            # --- PEDIR Y VALIDAR NOMBRE ---
            nombre = input("Ingrese el nombre del estudiante: ").strip()
            if not Estudiante.validar_nombre(nombre):
                raise ValueError("Nombre inválido. Debe contener solo letras y tener al menos 2 caracteres.")
            
            # --- PEDIR Y VALIDAR EDAD ---
            edad_str = input("Ingrese la edad del estudiante: ")
            if not edad_str.isdigit():
                raise ValueError("La edad debe ser un número.")
            edad = int(edad_str)
            if not Estudiante.validar_edad(edad):
                raise ValueError("Edad inválida. Debe ser un entero entre 16 y 25.")

            # --- CREAR Y AGREGAR ESTUDIANTE ---
            nuevo_estudiante = Estudiante(matricula, nombre.title(), edad)
            self.lista_estudiantes.append(nuevo_estudiante)
            print(f"Estudiante {nuevo_estudiante.nombre} agregado con éxito.")

        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

    #Metodo para agregar profesores
    def agregar_profesor(self):
        try:
            print("\n=== AGREGAR NUEVO PROFESOR ===")
            
            # --- PEDIR Y VALIDAR DATOS DEL PROFESOR ---
            matricula = input("Ingrese la matrícula del profesor: ").strip()
            if not matricula:
                raise ValueError("La matrícula no puede estar vacía")
            
            # --- VERIFICAR QUE NO EXISTA YA EL PROFESOR ---
            if any(prof.matricula == matricula for prof in self.lista_profesores):
                raise ValueError(f"Ya existe un profesor con matrícula {matricula}")
            
            nombre = input("Ingrese el nombre del profesor: ").strip()
            if not nombre:
                raise ValueError("El nombre no puede estar vacío")
            elif nombre.isdigit():
                raise ValueError("El nombre no debe ser numeros")
            
            edad_str = input("Ingrese la edad del profesor: ").strip() #strip() elimina espacios en blanco al inicio y final
            if not edad_str.isdigit():
                raise ValueError("La edad debe ser un número")
            edad = int(edad_str)
            
            if not (18 <= edad <= 70):
                raise ValueError("La edad debe estar entre 18 y 70 años")
            
            especialidad = input("Ingrese la especialidad del profesor: ").strip()
            if not especialidad:
                raise ValueError("La especialidad no puede estar vacía")
            
            # --- CREAR Y AGREGAR PROFESOR ---
            nuevo_profesor = Profesor(matricula, nombre.title(), edad, especialidad.title())
            self.lista_profesores.append(nuevo_profesor)
            print(f"Profesor {nombre} agregado exitosamente con matrícula {matricula}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    #Metodo para agregar materias
    def agregar_materia(self):
        try:
            print("\n=== AGREGAR NUEVA MATERIA ===")
            
            if not self.lista_profesores:
                print("No hay profesores registrados. Debe agregar un profesor primero.")
                return
            
            # --- MOSTRAR PROFESORES DISPONIBLES ---
            print("\nProfesores disponibles:")
            for i, profesor in enumerate(self.lista_profesores, 1):
                print(f"{i}. {profesor.nombre} - {profesor.especialidad} (Matrícula: {profesor.matricula})")
            
            # --- PEDIR Y VALIDAR DATOS DE LA MATERIA ---
            nombre_materia = input("\nIngrese el nombre de la materia: ").strip()
            if not nombre_materia:
                raise ValueError("El nombre de la materia no puede estar vacío")
            
            # --- VERIFICAR QUE NO EXISTA YA LA MATERIA ---
            if any(mat.nombre.lower() == nombre_materia.lower() for mat in self.lista_materias):
                raise ValueError(f"Ya existe la materia {nombre_materia}")
            
            # --- PEDIR MATRÍCULA DEL PROFESOR ---
            matricula_profesor = input("Ingrese la matrícula del profesor que impartirá la materia: ").strip()
            
            # --- BUSCAR EL PROFESOR ---
            profesor = next((prof for prof in self.lista_profesores 
                            if prof.matricula == matricula_profesor), None)
            
            if not profesor:
                raise ValueError(f"No se encontró profesor con matrícula {matricula_profesor}")
            
            # --- CREAR Y AGREGAR MATERIA ---
            nueva_materia = Materia(nombre_materia.title(), profesor)
            self.lista_materias.append(nueva_materia)
            
            print(f"Materia {nombre_materia} agregada exitosamente")
            print(f"Profesor asignado: {profesor.nombre}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    #Metodo para mostrar estudiantes
    def mostrar_estudiantes(self):
        for estudiante in self.lista_estudiantes: # Recorro la lista de estudiantes
            estudiante.mostrar_datos()            # Llamo al metodo mostrar_datos de cada estudiante

    #Metodo para mostrar profesores
    def mostrar_profesores(self):
        for profesor in self.lista_profesores:   # Recorro la lista de profesores
            profesor.mostrar_datos()             # Llamo al metodo mostrar_datos de cada profesor

    #Metodo para mostrar materias
    def mostrar_materias(self):
        for materia in self.lista_materias:     # Recorro la lista de materias
            print(f"Materia: {materia.nombre}, Profesor: {materia.profesor.nombre}") # Muestro el nombre de la materia y el nombre del profesor

    #Metodo pra mostrar estudiantes aprobados en una materia
    def mostrar_estudiantes_aprobados(self, calificacion_minima=60):
        try:
            #--- MOSTRAR LA LISTA DE MATERIAS ---
            if not self.lista_materias:
                print("No hay materias registradas.")
                return
            
            print("\n----Materias Disponibles")
            for num, materia in enumerate(self.lista_materias, start=1):
                print(f"{num}. {materia.nombre}")

            #--- PEDIR EL NOMBRE DE LA MATERIA ---
            nombre_materia = input("\nIngrese el nombre de la materia: ").strip()
            if not nombre_materia:
                raise ValueError("El nombre de la materia no puede estar vacio")
            
            #--- BUSCAR LA MATERIA ---
            materia = next((mat for mat in self.lista_materias if mat.nombre.lower() == nombre_materia.lower()), None)

            if not materia:
                print(f"No se encontro la materia: {nombre_materia}")
                return
            
            #--- OBTENER Y MOSTRAR ESTUDIANTES APROBADOS ---
            estudiantes_aprobados = materia.estudiantes_aprobados(calificacion_minima)

            if not estudiantes_aprobados:
                print(f"No hay estudiantes aprovados en la {materia.nombre}")
                return
            
            print(f"\n-----ESTUDIANTES APROBADOS EN {materia.nombre.upper()}-------")
            for estu in estudiantes_aprobados:
                promedio = estu.calcular_promedio()
                print(f"-{estu.nombre} (Matricula: {estu.matricula}) - Promedio: {promedio:.2f}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    #Metodo para mostrar estudiantes reprobados en una materia
    def mostrar_estudiantes_reprobados(self, calificacion_minima=60):       
        try:
            if not self.lista_materias:
                print("No hay materias registradas")
                return
            
            print(f"\n----ESTUDIANTES REPROBADOS----------")

            # Variable para rastrear si hay reprobados en alguna materia
            reprobados = False
            for materia in self.lista_materias:
                estudiante_aprobados = materia.estudiantes_aprobados(calificacion_minima)
                # Filtrar estudiantes reprobados
                estudiante_reprobados = [estu for estu in materia.lista_estudiantes if estu not in estudiante_aprobados]

                if estudiante_reprobados:
                    reprobados = True
                    #--- Mostrar estudiantes reprobados en esta materia ---
                    print(f"\n MATERIA: {materia.nombre}")
                    print(f"   Profesor: {materia.profesor.nombre}")
                    for estudiante in estudiante_reprobados:
                        promedio = estudiante.calcular_promedio()
                        print(f" {estudiante.nombre} - Promedio: {promedio:.2f}")
            
            if not reprobados:
                print("No hay estudiantes reprobados en ninguna materia.")
                
        except Exception as e:
            print(f"Error inesperado: {e}")
                    
    #Metodo para agregar un estudiante a una materia
    def agregar_estudiante_a_materia(self):
        try:
            print("\n=== INSCRIBIR ESTUDIANTE EN MATERIA ===")
            
            # --- VERIFICAR QUE HAYA ESTUDIANTES Y MATERIAS ---
            if not self.lista_estudiantes:
                print("No hay estudiantes registrados.")
                return
                
            if not self.lista_materias:
                print("No hay materias registradas.")
                return
            
            #--- MOSTRAR ESTUDIANTES DISPONIBLES ---
            print("\nESTUDIANTES DISPONIBLES:")
            for i, estudiante in enumerate(self.lista_estudiantes, 1):
                promedio = estudiante.calcular_promedio()
                total_materias = len(estudiante.calificaciones)
                print(f"{i:2}. {estudiante.nombre:<15} (Matrícula: {estudiante.matricula}) - Promedio: {promedio:5.2f} - Materias: {total_materias}")
            
            #--- PEDIR LA MATRÍCULA DEL ESTUDIANTE ---
            matricula = input("\nIngrese la matrícula del estudiante: ").strip()
            
            #--- BUSCAR EL ESTUDIANTE ---
            estudiante = next((est for est in self.lista_estudiantes 
                            if str(est.matricula).lower() == matricula.lower()), None)
            
            if not estudiante:
                raise ValueError(f"No se encontró estudiante con matrícula: {matricula}")  #  Correcto
            
            #--- MOSTRAR MATERIAS DISPONIBLES ---
            print(f"\nMATERIAS DISPONIBLES:")
            for i, materia in enumerate(self.lista_materias, 1):
                inscritos = len(materia.lista_estudiantes)
                ya_inscrito = "YA INSCRITO" if estudiante in materia.lista_estudiantes else "Disponible"
                print(f"{i:2}. {materia.nombre:<15} (Profesor: {materia.profesor.nombre:<12}) - Inscritos: {inscritos:2} - {ya_inscrito}")
            
            #--- PEDIR EL NOMBRE DE LA MATERIA ---
            nombre_materia = input("\nIngrese el nombre de la materia: ").strip()
            if not nombre_materia:
                raise ValueError("El nombre de la materia no puede estar vacío")
            
            # Buscar la materia
            materia = next((mat for mat in self.lista_materias 
                        if mat.nombre.lower() == nombre_materia.lower()), None)
            
            if not materia:
                print(f"No se encontró la materia: '{nombre_materia}'")  # ✅ CORRECTO
                return
            
            #--- VERIFICAR SI EL ESTUDIANTE YA ESTÁ INSCRITO ---
            if estudiante in materia.lista_estudiantes:
                print(f"El estudiante {estudiante.nombre} ya está inscrito en {materia.nombre}")
                return
            
            #--- INSCRIBIR AL ESTUDIANTE ---
            if materia.agregar_estudiante(estudiante):
                print(f"{estudiante.nombre} ha sido inscrito exitosamente en {materia.nombre}")
                print(f"   Profesor: {materia.profesor.nombre}")
                print(f"   Total de estudiantes en la materia: {len(materia.lista_estudiantes)}")
                
                #-- Mostrar otros estudiantes inscritos en la materia ---
                if len(materia.lista_estudiantes) > 1:
                    print(f"   Otros estudiantes inscritos:")
                    for est in materia.lista_estudiantes:
                        if est != estudiante:
                            print(f"- {est.nombre}")
            else:
                print(f"No se pudo inscribir al estudiante (posible error interno)")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as x:
            print(f"Error inesperado: {x}")

    #Metodo para agregar calificaciones a un estudiante
    def agregar_calificacion_estudiante(self):
        try:
            
            #--- VERIFICAR QUE HAYA ESTUDIANTES ---
            if not self.lista_estudiantes:
                print("No hay estudiantes registrados.")
                return

            print("\n----LISTA DE ESTUDIANTES----")
            for i, estu in enumerate(self.lista_estudiantes, start=1):
                print(f"{i}. {estu.nombre} (Matricula: {estu.matricula})")

            #--- PEDIR EL NOMBRE DEL ESTUDIANTE ---
            nombre_estudiante = input("Ingrese el nombre del estudiante al que desea agregar calificaciones: ").strip()
            if not nombre_estudiante:
                raise ValueError("El nombre del estudiante no puede estar vacio.")
            
            #--- BUSCAR EL ESTUDIANTE ---
            estudiante = next((est for est in self.lista_estudiantes if est.nombre.lower() == nombre_estudiante.lower()), None)
            if not estudiante:
                print(f"No se encontro el estudiante con el nombre {nombre_estudiante}.")
                return

            #--- PEDIR LOS DATOS DE LA MATERIA Y CALIFICACIÓN ---
            print(f"\nAgregando calificaciones para {estudiante.nombre}:")
            materia = input("Ingrese el nombre de la materia: ").strip()
            if not materia:
                raise ValueError("El nombre de la materia no puede estar vacio.")
            
            calificacion = float(input("Ingrese la calificacion (0-100): "))
            if not (0 <= calificacion <= 100):
                raise ValueError("La calificacion debe estar entre 0 y 100.")
            
            # BUSCAR LA MATERIA
            materia_obj = next((mat for mat in self.lista_materias if mat.nombre.lower() == materia.lower()), None)
            
            # ¡NUEVA LÓGICA! para inscribir al estudiante si no está inscrito
            
            if materia_obj and estudiante not in materia_obj.lista_estudiantes:
                print(f"Advertencia: {estudiante.nombre} no está inscrito en {materia_obj.nombre}.")
                inscribir = input("¿Desea inscribirlo ahora? (s/n): ").strip().lower()
                if inscribir in ['s', 'si', 'sí']:
                    materia_obj.agregar_estudiante(estudiante)
                    print(f"{estudiante.nombre} ha sido inscrito en {materia_obj.nombre}.")
            
            #--- AGREGAR LA CALIFICACIÓN ---
            estudiante.agregar_calificacion(materia, calificacion)
            print(f"Calificacion {calificacion} agregada a {estudiante.nombre} en la materia {materia}.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


    ##Metodo para ver las calificacione del estudiante
    def ver_calificaciones_estudiante(self):
        try:
            #--- MOSTRAR LA LISTA DE ESTUDIANTES ---
            print("\n----LISTA DE ESTUDIANTES----")
            for est in self.lista_estudiantes:
                print(f"- {est.nombre} (Matricula: {est.matricula})")

            #--- PEDIR LA MATRÍCULA DEL ESTUDIANTE ---
            matricula = input("Ingrese la matricula del estudiante para ver sus calificaciones: ").strip()
            if not matricula:
                raise ValueError("La matricula no puede estar vacia.")
            
            #Buscar el estudiantes por matricula    
            estudiante = next((est for est in self.lista_estudiantes if est.matricula == matricula), None)
            if not estudiante:
                print(f"No se encontro el estudiante con la matricula {matricula}.")
                return      
            
            #Mostrar las calificaciones del estudiante
            if estudiante:
                print(f"\nCalificaciones de {estudiante.nombre}:")
                if estudiante.calificaciones:
                    for materia, calificacion in estudiante.calificaciones.items():
                        print(f"- {materia}: {calificacion}")
                    print(f"Promedio General: {estudiante.calcular_promedio():.2f}")
                else:
                    print("No hay calificaciones registradas para este estudiante.")    
            else:
                print(f"No se encontro el estudiante con la matricula {matricula}.")
                return
        except ValueError as e:
            print(f"Error: {e}")
        
