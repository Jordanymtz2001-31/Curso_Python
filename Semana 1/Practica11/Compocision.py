#Ejemplo de composicion

class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def encender(self):
        print(f"El motor {self.tipo} ha encendido de {self.potencia} HP esta encendido.")

class Coche:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor  # Composición: un coche tiene un motor

    def arrancar(self):
        print(f"Arranca el coche {self.marca} -- {self.modelo}.....")
        self.motor.encender() # Llamada al método del motor y se muestra el mensaje

#Instacia de la clase Motor
motor_electrico = Motor("Eléctrico", 150)

#Instacia de la clase Coche con el motor_electrico
mi_coche = Coche("Tesla", "Model 3", motor_electrico)

#Arrancar el coche
mi_coche.arrancar()