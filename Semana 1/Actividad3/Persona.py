#Crear una clase Persona (Clase padre): Clave, Nombre, Edad

class Persona:
    def __init__(self, clave, nombre, edad):
        self._clave = clave
        self._nombre = nombre
        self._edad = edad

    def __str__(self):
        return f"Clave: {self._clave}, Nombre: {self._nombre}, Edad: {self._edad}"

    @property
    def clave(self):
        return self._clave
    @clave.setter
    def clave(self, valor):
        self._clave = valor

    @property
    def nombre(self):
        return self._nombre 
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        self._edad = valor

#Crear una clase Usuario (Clase hija): Libros prestados []

class Usuario(Persona):
    def __init__(self, clave, nombre, edad):
        super().__init__(clave, nombre, edad)
        self._libros_prestados = []

    def __str__(self):
        return f"{super().__str__()}, Libros Prestados: {len(self._libros_prestados)}"
    

    def pedir_prestados_libro(self, libro):

        #Limitar a un maximo de 3 libros prestados
        if len(self._libros_prestados) == 3:
            print(f"{self.nombre} ya tienes 3 libros")
            return False

        if libro.titulo not in self._libros_prestados and libro.disponible: # Evitar duplicados
            self._libros_prestados.append(libro.titulo) # Agregar libro a la lista
            libro.disponible = False # Marcar libro como no disponible
            print(f"Libro {libro.titulo} prestado a {self.nombre}.")
            return True
        elif not libro.disponible:
            print(f"El libro {libro.titulo} no está disponible para préstamo.")
            return False
        else:
            print(f"El libro {libro.titulo}  no existe.")
            return False

    def devolver_libro(self, libro):
        if libro.titulo in self._libros_prestados: # Verificar si el libro está prestado
            self._libros_prestados.remove(libro.titulo) # Eliminar libro de la lista
            libro.disponible = True # Marcar libro como disponible
            print(f"Libro {libro.titulo} devuelto por {self.nombre}.")
            return True
        else:
            print(f"El libro {libro.titulo} no está prestado a {self.nombre}.")
            return False
    
#Crear una clase Libro: Id, Titulo, Autor, disponible (Booleano)

class Libro:
    def __init__(self, id, titulo, autor, disponible=True):
        self._id = id
        self._titulo = titulo
        self._autor = autor
        self._disponible = disponible

    def __str__(self):
        return f"ID: {self._id}, Titulo: {self._titulo}, Autor: {self._autor}, Disponible: {self._disponible}"

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor

    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, valor):
        self._autor = valor

    @property
    def disponible(self):
        return self._disponible
    
    @disponible.setter      
    def disponible(self, valor):
        self._disponible = valor

#Crear una clase Biblioteca: Nombre, Lista de usuarios, lista de libros

class Biblioteca:
    def __init__(self, nombre):
        self._nombre = nombre
        self.usuarios = []
        self.libros = []
    
    @property
    def nombre(self):
        return self._nombre

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_usuario(self, nombre):
        nombre = nombre.strip().lower()
        for usuario in self.usuarios:
            if usuario.nombre.strip().lower() == nombre:
                return usuario
        return None

    def eliminar_usuario(self, nombre_usuario):
        for usuario in self.usuarios:
            if usuario.nombre == nombre_usuario:
                self.usuarios.remove(usuario)
                print(f"Usuario {nombre_usuario} eliminado.")
                return
        print(f"Usuario {nombre_usuario} no encontrado.")
    
    def eliminar_libro(self, libro):
        for libro in self.libros:
            if libro._titulo == libro._titulo:
                self.libros.remove(libro)
                print(f"Libro con nombre {libro._titulo} eliminado.")
                return
        print(f"Libro con nombre {libro._titulo} no encontrado.")

    def __str__(self):
        return f"Biblioteca: {self.nombre}, Usuarios: {len(self.usuarios)}, Libros: {len(self.libros)}"
