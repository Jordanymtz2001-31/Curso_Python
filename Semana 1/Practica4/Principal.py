from Escuela import Escuela

class Principal:

    def __init__(self):
        
        #Creamos lista
        self.list_escuela = []

        #Creamos instancias
        escuela1 = Escuela("Escuela A", "Primaria", "Puebla", "Publica")
        escuela2 = Escuela("Escuela B", "Secundari", "CDMX", "Publica")
        escuela3 = Escuela("Escuela C", "Bachiller", "Oaxaca", "Privada")
        escuela4 = Escuela("Escuela D", "Universiad", "Jalisco", "Privada")
        escuela5 = Escuela("Escuela E", "Primaria", "Tabasco", "Publica")

        #Guardamos
        self.list_escuela.extend([escuela1, escuela2, escuela3, escuela4, escuela5])
    def menu(self):
        while True:
            print("\n--- Menu de Opciones ---")
            print("1.- Ingresar escuela")
            print("2.- Lista escuela")
            print("3.- Buscamos escuela por indice")
            print("4.- Editamos escuela por indice")
            print("5.- Eliminamos escuela por indice")
            print("6.- Salir")

            opcion = input("Seleccione una opción (1-6): ")

            match opcion:
                case "1":
                    self.ingresar_escuela()
                case "2":
                    self.lista_escuela()
                case "3":
                    self.buscar_escuela()
                case "4":
                    self.editar_escuela()
                case "5":
                    self.eliminar_ecuela()
                case "6":
                    print("Saliendo del programa")
                    break
                case _:
                    print("Opcion invalidad, intente de nuevo")
    
    def ingresar_escuela(self):
        #Pedimos los datos
        nombre = input("Nombre de la escuela: ")
        nivel = input("Nivel: (Primaria, secundaria, Bachiller, Universidad) ")
        estado = input("Estado de la republica: ")
        tipo = input("Tipo (Privada/Publica) ")

        #Cremamos el objeto
        New_escuela = Escuela(nombre, nivel, estado, tipo)
        #Agregamos a la lista
        self.list_escuela.append(New_escuela)
        print("Escuela registrada correctamente")

    def lista_escuela(self):
        if len(self.list_escuela) == 0:
            print("No hay escuelas")
        else:
            for i, escuela in enumerate(self.list_escuela):
                print(f"{i}.-{escuela}")
    
    def buscar_escuela(self):
        indide = int(input("Ingresa el indice de la escuela quieres buscar: "))
        print(self.list_escuela[indide])

    def editar_escuela(self):
        indice = int(input("Ingresa el indice de la escuela que desea editar"))
        escuela = self.list_escuela[indice]

        print("\nIngresa los nuevos valores y deja en blando los valores que no quieres cambiar\n")

        #Solicitamos los valores o si no se mete los valores que obtenga el que ya tiene
        nombre = input(f"Nuevo nombre({escuela.get_nombre()}): ") or escuela.get_nombre()
        nivel = input(f"Nuevo nivel({escuela.get_nivel()}): ") or escuela.get_nivel()
        estado = input(f"Nuevo Estado({escuela.get_estado()}): ") or escuela.get_estado()
        tipo = input(f"Nuevo Tipo({escuela.get_tipo()}): ") or escuela.get_tipo()

        #Metemos los velores a la escuela
        escuela.set_nombre(nombre)
        escuela.set_nivel(nivel)
        escuela.set_estado(estado)
        escuela.set_tipo(tipo)

        print("\nEscuela editada exitosamente\n")
    
    def eliminar_ecuela(self):
        indice = int(input("Ingresa el indice que deseas eliminar: "))
        self.list_escuela.pop(indice)
        print("Escuela eliminada correctamente")

if __name__ == "__main__":
    app = Principal() #Creamos una instancia
    app.menu() #Llamamos a la funcion


