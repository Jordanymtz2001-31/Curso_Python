from Transporte import Transporte
from Conductor import Conductor
from Avion import Avion
from Barco import Barco
from Moto import Moto
from Choche import Coche



def main():

    #Aqui creas el objeto de Conductor
    conductor1 = Conductor("Pedro", "A12345", "Aviones")
    conductor2 = Conductor("Luis", "B67890", "Avionetas")
    conductor3 = Conductor("Juan", "C54321", "Camiones")   
    conductor4 = Conductor("Max", "A25WE5", "Motos y Autos") 
    conductor5 = Conductor("Melany", "A2F3FE3", "Barcos")
    conductor6 = Conductor("Dany", "EW2W3", "Motos")
    conductor7 = Conductor("Emilio", "R2VRE", "Cruseros")

    # Aquí creas el objeto Avion
    avion1 = Avion("Avion1", "Mediano", "Aereo", conductor1, 2001)
    avion2 = Avion("Avion2", "Pequeño", "Aereo", conductor2, 2002)

    # Aquí creas el objeto Barco
    barco1 = Barco("Barco1", "Grande", "Marítimo", conductor5, 1800)
    barco2 = Barco("Barco2", "Pequeño", "Marítimo", conductor7, 1752)

    # Aquí creas el objeto Moto
    moto1 = Moto("Moto1", "Pequeña", "Terrestre", conductor4, "Yamaha R1")
    moto2 = Moto("Moto2", "Mediana", "Terrestre", conductor6, "Vespa LX")

    # Aquí creas el objeto Coche
    coche1 = Coche("Coche1", "Grande", "Terrestre", conductor3, "Toyota Camry")
    coche2 = Coche("Coche2", "Mediana", "Terrestre", conductor4, "Honda CR-V")


    #lista de conductores
    lis_conductores = [conductor1, conductor2, conductor3, conductor4, conductor5, conductor6, conductor7]

    # Listas para almacenar 
    lis_avion = [avion1, avion2]
    lis_barco = [barco1, barco2]
    lis_moto = [moto1, moto2]
    lis_coche = [coche1, coche2]
    #Creamos el Menu

    while True:
        print("\n-----Menu de Transportes-----\n")
        print("1.- Agregar un conductor a un transporte")
        print("2.- Mostrar por tipo de transporte")
        print("3.- Mostrar todos los conductores")
        print("4.- Eliminar un transporte")
        print("5.- Eliminar un conductor")
        print("6.- Salir\n")

        opcion = input("Seleccione una opcion por favor (1-6): ")
        match opcion:
            case "1":
                print("\n--- Tipos de Transporte ---")
                print("1. Avión")
                print("2. Barco")
                print("3. Coche")
                print("4. Moto")
                tipo_opcion = input("\nSeleccione el tipo de transporte: ")

                tipo = input("Ingrese el tipo de transporte: ")
                tamaño = input("Ingrese el tamaño del transporte: ")
                area = input("Ingrese el area: ")

                #Registrar el conductor que manejara ese transporte
                nombre_conductor = input("\nNombre del conductor: ")
                licencia_conductor = input("Licencia del conductor: ")
                especialidad_conductor = input("Especialidad del conductor: ")

                #Crear el nuevo conductor
                conductor = Conductor(nombre_conductor, licencia_conductor, especialidad_conductor)
                lis_conductores.append(conductor)

                #Segun lo que eliga
                if tipo_opcion == "1":
                    año_modelo = input("Ingrese el año de modelo del avión: ")
                    nuevo_transporte = Avion(tipo, tamaño, area, conductor, año_modelo)
                    lis_avion.append(nuevo_transporte)
                elif tipo_opcion == "2":
                    año_modelo = input("Ingrese el año de modelo del barco: ")
                    nuevo_transporte = Barco(tipo, tamaño, area, conductor, año_modelo)
                    lis_barco.append(nuevo_transporte)
                elif tipo_opcion == "3":
                    año_modelo = input("Ingrese el año de modelo del coche: ")
                    nuevo_transporte = Coche(tipo, tamaño, area, conductor, año_modelo)
                    lis_coche.append(nuevo_transporte)
                elif tipo_opcion == "4":
                    año_modelo = input("Ingrese el año de modelo de la moto: ")
                    nuevo_transporte = Moto(tipo, tamaño, area, conductor, año_modelo)
                    lis_moto.append(nuevo_transporte)
                else:
                    print("Opción de transporte no válida.")
                    return
            
                print(f"\nTransporte agregado correctamente con su Conductor {nombre_conductor}")

                
            case "2":
                print("\n--- Mostrar Transportes por Tipo ---")
                print("1. Avión")
                print("2. Barco")
                print("3. Coche")
                print("4. Moto")
                tipo_opcion = input("\nSeleccione el tipo de transporte: ")

                match tipo_opcion:
                    case "1":
                        if not lis_avion:
                            print("No hay aviones registrados.")
                        for avion in lis_avion:
                            print(avion)
                    case "2":
                        if not lis_barco:
                            print("No hay barcos registrados.")
                        for barco in lis_barco:
                            print(barco)
                    case "3":
                        if not lis_coche:
                            print("No hay coches registrados.")
                        for coche in lis_coche:
                            print(coche)
                    case "4":
                        if not lis_moto:
                            print("No hay motos registradas.")
                        for moto in lis_moto:
                            print(moto)
                            
                    case _:
                        print("Opción no válida.")


            case "3":
                print("\n--- Lista de Conductores ---")
                if not lis_conductores:
                        print("No hay conductores registrados.")
                else:
                        for conductor in lis_conductores:
                            print(conductor)
            case "4":
                print("\n-----Eliminar Transporte-----")
                print("1.- Avion")
                print("2.- Barco")
                print("3.- Coche")
                print("4.- Moto")

                tip_opcion = input("Selecione el tipo de Transporte: ")

                # Selecciona la lista correspondiente
                if tip_opcion == "1":
                    lista = lis_avion
                    nombre = "avión"
                elif tip_opcion == "2":
                    lista = lis_barco
                    nombre = "barco"
                elif tip_opcion == "3":
                    lista = lis_coche
                    nombre = "coche"
                elif tip_opcion == "4":
                    lista = lis_moto
                    nombre = "moto"
                else:
                    print("Opción no válida.")
                    return

                if not lista:
                    print(f"No hay {nombre}s registrados.")
                    return
                
                print(f"\n---Lista de {nombre}: ")
                for nun, transport in enumerate(lista, start=1):
                    print(f"\n{nun} - {transport}")

                opcion = input(f"Seleciona el numero de {nombre} a eliminar: ")

                #Verificamos si lo que puso el usuario cumple
                try:
                    num = int(opcion)  - 1
                    if 0 <= num < len(lista):
                        elim = lista.pop(num)
                        print(f"Transporte {elim} Eliminado Exitosamente")
                    else:
                        print("Error: Debes de colocar numeros dentro del rango")
                except ValueError:
                    print("Error: Solo numeros")
            case "5":
                print("\n---Eliminar Conductor-----")
                if not lis_conductores:
                    print("No hay conductores registrado")
                    return
                
                print("Conductores registrados:")
                for num, conductor in enumerate(lis_conductores, start=1):
                    print(f"{num}. {conductor}")

                opcion = input("Selecciona el numero de conductor a eliminar")

                try:
                    num = int(opcion) - 1
                    if 0 <= num < len(lis_conductores):
                        eliminar = lis_conductores.pop(num)
                        print(f"Conductor {eliminar} eliminado correctamente")
                    else:
                        print("Fuera de rango")

                except ValueError:
                    print("Error: Solo enteros")
            case "6":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    main()
