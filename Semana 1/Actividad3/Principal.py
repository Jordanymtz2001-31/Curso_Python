from unittest import case
from Persona import Persona, Libro, Usuario, Biblioteca


class Principal:

    def __init__(self):
        self.biblioteca = Biblioteca("Biblioteca Benito")

    def menu(self):
        while True:
            print("\n--- Menu Principal ---")
            print("1.- Registrar Usuario")
            print("2.- Registrar Libro")
            print("3.- Listar libros de un usuario")
            print("4.- Listar usuarios de la biblioteca")
            print("5.- Listar libros de la biblioteca")
            print("6.- Prestar libro a un usuario")
            print("7.- Devolver libro de un usuario")
            print("8.- Eliminar usuario")
            print("9.- Eliminar libro")
            print("0.- Salir")

            opcion = input("Seleccione una opción (0-9): ")
            match opcion:
                case "1":
                    self.registrar_usuario()
                case "2":
                    self.registrar_libro()
                case "3":
                    self.listar_libros_usuario()
                case "4":
                    self.listar_usuarios()
                case "5":
                    self.listar_libros()
                case "6":
                    self.prestar_libro()
                case "7":
                    self.devolver_libro()
                case "8":
                    self.eliminar_usuario()
                case "9":
                    self.eliminar_libro()
                case "0":
                    print("Saliendo del programa")
                    break
                case _:
                    print("Opción inválida, intente de nuevo")

        #Creamos la funcion para registrar usuario
    def registrar_usuario(self):
        id_usuario = input("ID del usuario: ").strip().lower()
        nombre = input("Nombre del usuario: ")
        edad = input("Edad del usuario: ")
        #Creamos el nuevo usuario
        nuevo_usuario = Usuario(id_usuario, nombre, edad)
        self.biblioteca.agregar_usuario(nuevo_usuario) #Agregamos a la biblioteca
        print(f"Usuario {nombre} registrado exitosamente.")

    #Creamos la funcion para registrar libro
    def registrar_libro(self):
        id_libro = input("ID del libro: ")
        titulo = input("Título del libro: ")
        autor = input("Autor del libro: ")
        disponible = True
        #Creamos el nuevo libro
        nuevo_libro = Libro(id_libro, titulo, autor, disponible)
        self.biblioteca.agregar_libro(nuevo_libro) #Agregamos a la biblioteca
        print(f"Libro {titulo} registrado exitosamente.")
    
    #Creamos la funcion para listar libros de un usuario por nombre
    def listar_libros_usuario(self):
        nombre = input("Dime el nombre del usuario:")
        usuario = self.biblioteca.buscar_usuario(nombre) #Buscamo el nombre
        if usuario:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario._libros_prestados: # Imprimir los libros prestados
                print(libro)
        else:
            print(f"Usuario {nombre} no encontrado.")

    #Creamos la funcion para listar usuarios
    def listar_usuarios(self):
        if len(self.biblioteca.usuarios) == 0: #Si en bibloteca no tiene usuarios
            print("No hay usuarios registrados.")
        else:
            print("Usuarios registrados:")
            for usuario in self.biblioteca.usuarios:
                print(usuario)

    #Creamos la funcion para listar libros
    def listar_libros(self):
        if len(self.biblioteca.libros) == 0:
            print("No hay libros registrados.")
        else:
            print("Libros registrados:")
            for libro in self.biblioteca.libros:
                print(libro)
    
    #Creamos la funcion para prestar libro
    def prestar_libro(self):
        nombre_usuario = input("Nombre del usuario que va a recibir el libro: ").strip()
        nombre_libro = input("Titulo del libro a prestar: ")
        usuario = self.biblioteca.buscar_usuario(nombre_usuario) # Buscar usuario
        if usuario: # Si se encuentra el usuario
            print(f"Usuario encontrado: {nombre_usuario}.")
        else:
            print("Usuario no encontrado.")
            return
        # Buscar libro disponible
        # Con next obtenemos el primer libro que cumpla la condicion
        # Y con el for buscamos en la lista de libros de la biblioteca
        libro = next(lib for lib in self.biblioteca.libros if lib.titulo == nombre_libro)

        if not libro: # Si no se encuentra el libro
            print(f"Libro {nombre_libro} no encontrado o no disponible.")
            return
        # Prestar el libro
        libro.disponible = False
        usuario.pedir_prestados_libro(libro)

    #Creamos la funcion para devolver libro
    def devolver_libro(self):
        nombre_usuario = input("Nombre del usuario que va a devolver el libro: ")
        nombre_libro = input("Nombre del libro a devolver: ")
        usuario = self.biblioteca.buscar_usuario(nombre_usuario) # Buscar usuario

        if not usuario: # Si no se encuentra el usuario
            print(f"Usuario {nombre_usuario} no encontrado.")
            return
        # Buscar libro en los libros prestados del usuario
        libro = next(lib for lib in self.biblioteca.libros if lib.titulo == nombre_libro)
        if not libro: # Si no se encuentra el libro
            print(f"Libro {nombre_libro} no encontrado.")
            return
        
        #Llamamos al metodo devolver libro del usuario
        usuario.devolver_libro(libro)
    
    #Creamos la funcion para eliminar usuario
    def eliminar_usuario(self):
        nombre =  input("Dime el nombre del usuario a eliminar: ")
        self.biblioteca.eliminar_usuario(nombre)

    #Creamos la funcion para eliminar usuario
    def eliminar_libro(self):
        libro = input("Dime el nombre del libro a eliminar: ")
        self.biblioteca.eliminar_libro(libro)

if __name__ == "__main__":
    app = Principal()
    app.menu()