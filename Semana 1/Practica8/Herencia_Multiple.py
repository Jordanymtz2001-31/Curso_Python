#Herencia Múltiple: una clase hija que hereda de dos o más clases padre

class Ave:
    def volar(self):
        return "puede volar"
    
class Mamifero:
    def caminar(self):
        return "puede caminar"

class Murcielago(Ave, Mamifero):
    def detalles(self):
        return f"El murcielago {self.volar()} y {self.caminar()}"
    
#Instancia de la clase Murcielago
Murcielago1 = Murcielago()
print(Murcielago1.detalles())
