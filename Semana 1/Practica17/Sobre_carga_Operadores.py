class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Sobre carga del operador +
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)
    
    #Sobre carga del operador -
    def __sub__(self, otro):
        return Punto(self.x - otro.x, self.y - otro.y)
    
    #Sobre carga del operador *
    def __mul__(self, escalar):
        return Punto(self.x * escalar, self.y * escalar)
    
    #Sobre carga del operador ==    
    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y
    
    #Sobre carga del operador /
    def __truediv__(self, escalar):
        if escalar == 0:
            raise ValueError("No se puede dividir por cero")
        return Punto(self.x / escalar, self.y / escalar)
    
    #Sobre carga del operador ><
    def __lt__ (self, otro):
        return (self.x**2 + self.y**2) < (otro.x**2 + otro.y**2)
    
    def __gt__ (self, otro):
        return (self.x**2 + self.y**2) > (otro.x**2 + otro.y**2)
    
    #Sobre carga de str
    def __str__(self):
        return f"Punto({self.x}, {self.y})"
    
p1 = Punto(2, 3)
p2 = Punto(4, 5)

print("Suma:", p1 + p2)
print("Resta:", p1 - p2)

p3 = Punto(6, 8)
print(f"Punto por escalar: {p3 * 2}")
print(f"Punto dividido por escalar: {p3 / 2}")

p1 = Punto(2, 3)
p2 = Punto(2, 3)
p3 = Punto(4, 5)

print(f"\n¿p1 es igual a p2?: {p1 == p2}")
print(f"¿p1 es menor que p3?: {p1 < p3}")
print(f"¿p1 es mayor que p3?: {p1 > p3}")

#Con la sobre carga de operadores podemos hacer operaciones con objetos de una manera intuitiva y sencilla.
#Con solo colocar el operador, este ya sabe que metodo llamar para realizar la operacion.