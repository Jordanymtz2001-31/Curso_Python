class Computadora:

    def __init__(self, marca, modelo, precio, ram, color):
        self._marca= marca
        self._modelo = modelo
        self._precio = precio
        self._ram = ram
        self._color = color

    def __str__(self):
        return f"Computadora: {self._marca} {self._modelo} {self._precio} {self._ram} {self._color}"
    
    @property #Getter
    def marca(self):
        return self._marca
    
    @marca.setter #Settter
    def marca(self, new_marca):
        self._marca = new_marca

    @property #Getter
    def modelo(self):
        return self._modelo
    
    @modelo.setter #Settter
    def modelo(self, new_modelo):
        self._marca = new_modelo

    @property #Getter
    def precio(self):
        return self._precio
    
    @precio.setter #Settter
    def precio(self, new_precio):
        self._precio = new_precio

    @property #Getter
    def ram(self):
        return self._ram
    
    @ram.setter #Settter
    def ram(self, new_ram):
        self._ram = new_ram

    @property #Getter
    def color(self):
        return self._color
    
    @color.setter #Settter
    def color(self, new_color):
        self._color = new_color



        