from abc import ABCMeta, abstractmethod

class ControlRemoto(metaclass=ABCMeta):
    @abstractmethod # A qui el @abstractmethod indica que el metodo es abstracto y debe ser implementado en las subclases
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def subir_volumen(self):
        pass

    @abstractmethod
    def bajar_volumen(self):
        pass

class Control_Samsung(ControlRemoto):
    def encender(self):
        print("La TV Samsung se ha encendido")

    def apagar(self):
        print("La TV Samsung se ha apagado")

    def subir_volumen(self):
        print("El volumen de la TV Samsung ha subido")

    def bajar_volumen(self):
        print("El volumen de la TV Samsung ha bajado")

class Control_LG(ControlRemoto):
    def encender(self):
        print("La TV LG se ha encendido")

    def apagar(self):
        print("La TV LG se ha apagado")

    def subir_volumen(self):
        print("El volumen de la TV LG ha subido")

    def bajar_volumen(self):
        print("El volumen de la TV LG ha bajado")

def main():
    samsung = Control_Samsung()
    lg = Control_LG()
    

    print("Control Samsung")
    samsung.encender()
    samsung.apagar()

    print("\nControl LG")
    lg.subir_volumen()
    lg.bajar_volumen()

    control = ControlRemoto()  #Aqui se genera un error porque no se puede instanciar una clase abstracta
    print("\nControl Remoto")
    control.encender()
    control.subir_volumen()
    control.bajar_volumen()
    control.apagar()

if __name__ == "__main__":
    main()