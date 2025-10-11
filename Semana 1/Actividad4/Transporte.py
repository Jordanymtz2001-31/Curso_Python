
class Transporte:
    def __init__(self, tipo, tamaño, area, conductor):
        self.tipo = tipo
        self.tamaño = tamaño
        self.area = area
        self.conductor = conductor

    def __str__(self):
        return f"El Transporte: {self.tipo}, de {self.tamaño} áreas en {self.area} con un {self.conductor}"
    

    def accion(self):
        return f"El transporte {self.tipo} esta despejando"
    
    def destino(self, destino):
        return f"El transporte {self.tipo} se dirige a {destino}"
    




