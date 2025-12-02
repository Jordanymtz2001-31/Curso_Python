class Escuela:

    #Contructor para la clase escuela y inicializacion de atributos
    def __init__(self, nombre, nivel, estado, tipo):
        self.nombre = nombre
        self.nivel = nivel
        self.estado = estado
        self.tipo = tipo

    def __str__(self):
        return f"Escuela: {self.nombre}-{self.nivel}, Ubicacion : {self.estado}, Tipo: {self.tipo}"
        
    #Set y getter
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, new_nombre):
        self.nombre = new_nombre

    def get_nivel(self):
        return self.nivel
    
    def set_nivel(self, new_nivel):
        self.nivel = new_nivel
    
    def get_estado(self):
        return self.estado
    
    def set_estado(self, new_estado):
        self.estado = new_estado

    def get_tipo(self):
        return self.tipo
    
    def set_tipo(self, new_tipo):
        self.nivel = new_tipo