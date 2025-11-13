from Productos import Productos

class Perecedero(Productos):
    def __init__(self, nombre, precio, dias_caducidad):
        super().__init__(nombre, precio)
        self._dias_caducidad = dias_caducidad

    def __str__(self):
        return super().__str__() + f"Días para caducar: {self._dias_caducidad}"
    
    @property
    def dias_caducidad(self):
        return self._dias_caducidad
    
    @dias_caducidad.setter
    def dias_caducidad(self, valor):
        self._dias_caducidad = valor
    
    #sobre escribimos el metodo calcular
    def calcular(self, cantidad):
        precio_final = super().calcular(cantidad)
        #Si el producto caduca en 5 dia, tiene un descuento del 50%
        if self.dias_caducidad <= 5:
            precio_final *= 0.5
            print("Se ha aplicado un descuento del 50% por caducidad" )
            print(f"Precio final con descuento: {precio_final:2f}")
        return precio_final
