from Medico import Medico
from Abogado import Abogado

def main():
    #Instancias de Abogado
    abogado1 = Abogado("Juan Perez", 40, 15, "Civil", "Despacho Legal ABC", 2000)

    #Instancias de Medico
    medico1 = Medico("Ana Gomez", 35, 10, "Cardiologia", "Consultorio 123", 2500)

    #Uso de Metodos
    print(abogado1)
    print(medico1)

    #Uso del metodo abstracto implementado
    abogado1.Mensaje()
    medico1.Mensaje()

    #Uso del metodo concreto
    print(abogado1.cobrar("Asesoría Legal", 1500))
    print(medico1.cobrar("Consulta Médica", 2500))  

if __name__ == "__main__":
    main()