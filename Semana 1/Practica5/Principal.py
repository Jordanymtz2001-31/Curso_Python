from Persona import Persona
from Medico import Medico
from Informatico import Informatico

def main():

    #Instancia
    persona = Persona("Juan Perez", 35, "Puebla")
    medico = Medico("Dr.Sergio Sanchez", 45, "Jalisco", "Neucirujano", 30000)
    informatico = Informatico("Pedro Lopez", 25, "Tabasco", "Analista", 20000)

    #Metodos de str
    print(persona)
    print(medico)
    print(informatico)

    #Metodos set
    informatico.nombre = "Dany"
    informatico.estado = "Michoaca"

    medico.nombre = "Melany"
    medico.edad = 22

    #Metodo getter
    print(f"\nHola soy: {informatico.nombre} y vivo en {informatico.estado}")
    print(f"Hola soy: {medico.nombre} y tengo {medico.edad}\n")

    print(informatico.trabajar("Full stack"))
    print(medico.trabajar())
    print(medico.trabajar("Medico cirujano", 40000)) 
       


if __name__ == "__main__":
    main()