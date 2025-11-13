#Simulacion de un interfaz informal
class ControlRemoto:
    def encender(self):
        pass
    def apagar(self):
        pass
    def subir_volumen(self):
        pass
    def bajar_volumen(self):
        pass

class Control_Samsung(ControlRemoto):
    
    def encender(self):
        print("La TV se ha encendido")
    
    def apagar(self):
        print("La TV se ha apagado")
    
    def subir_volumen(self):
        print("El volumen de la TV ha subido")
    
    def bajar_volumen(self):
        print("El volumen de la TV ha bajado")

class Control_LG(ControlRemoto):
    
    def encender(self):
        print("La TV se ha encendido")
    
    def apagar(self):
        print("La TV se ha apagado")


def main():

    #Interfaz informal
    samsung = Control_Samsung()
    lg = Control_LG()
    control = ControlRemoto()

    print("Control Samsung")
    samsung.encender()
    samsung.subir_volumen()

    print("\nControl LG")
    lg.encender()
    lg.bajar_volumen()  # This will not produce any output
    lg.subir_volumen()
    lg.apagar()
    
    print("\nControl Remoto")
    control.encender()


if __name__ == "__main__":
    main()