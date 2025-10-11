class Animal:
    
    def sonido(self):
        return "El sonido del "
    
class Perro(Animal):
    def sonido(self):
        return super().sonido() + "perro es: ¡Guau Guau!"
    
#Instancia de la clase Perro
Perro1 = Perro()
print(Perro1.sonido())