class Pato:

    def caminar(self):
        print("El pato está caminando.")

    def hablar(self):
        print("El pato está grasnando.")

class Gallina:

    def caminar(self):
        print("La gallina está caminando.")

    def hablar(self):
        print("La gallina está cacareando.")

class Cazador:

    def cazar(self, pato):
        pato.caminar()
        pato.hablar()
        print("¡Cazador ha cazado al animal!")

#instanciamos los objetos
pato = Pato()
gallina = Gallina()
cazador = Cazador()

cazador.cazar(pato) # El pato es cazado