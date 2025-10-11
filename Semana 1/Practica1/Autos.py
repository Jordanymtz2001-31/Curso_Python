class Autos:
    #Atributo de la clase
    cantidad_autos = 0
    #Metodo magido/dunder __init__ y __str__
    def __init__ (self, marca, modelo, año, color):
        self.marca = marca
        self.modelo =modelo
        self.año = año
        self.color = color
        Autos.incrementar_cantidad() #Llamada al metodo de clase para incrementar la cantidad de autos cada vez que se crea un nuevo objeto

    def __str__(self):
        return f"Auto: {self.marca} {self.modelo} {self.año} {self.color}"
    
    #Metodo de clase para manipular los atributos de la clase
    @classmethod #Este decorador indica que es un metodo de la case
    def incrementar_cantidad(cls):
        cls.cantidad_autos +=1

    @classmethod
    def mostrar_cantidad(cls):
        return f"Cantidad de autos: {cls.cantidad_autos}"
    
    #Metodos de instancia, obtener y modificar los atributos del objeto
    def get_marca(self):
        return self.marca
    
    def set_marca(self, new_marca):
        self.marca= new_marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, new_modelo):
        self.modelo= new_modelo

    def get_año(self):
        return self.año

    def set_año(self, new_año):
        self.año= new_año

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color= new_color
