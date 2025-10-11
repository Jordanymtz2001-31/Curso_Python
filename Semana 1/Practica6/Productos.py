class Productos:

    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    #Este metodo nos ayuda a imprimir el objeto
    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio:2f}"
    
    #el @property nos ayuda a crear getters y setters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        self._precio = valor

    #Funcion para calcular el precio total
    def calcular(self, cantidad):
        return self.precio * cantidad