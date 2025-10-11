from Mascotas import Mascota
from Canario import Canario
from Gato import Gato
from Perro import Perro

def main():

    #Polimorfismos
    mascotas = [
        Mascota("Pez", "Nemo"),
        Perro("Perro", "Sam", "Boxer"),
        Gato("Gato", "Bigotes", "Anaranjado"),
        Canario("Canario", "Alfonso", "Macho")
    ]

    for mascota in mascotas:
        print(mascota.hacer_ruido())
        print(mascota)
        print("-"*50)

if __name__ == "__main__":
    main()