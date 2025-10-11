from Computadora  import Computadora

class Principal:
    def main():

        #Se crea una lista
        comput_list = []

        compu1 = Computadora("HP", "Pavilion", 15000, "8GM", "Gris")
        compu2 = Computadora("ASUS", "Vivobook", 12000, "12GM", "Morado")
        compu3 = Computadora("DELL", "HP123", 11000, "16GM", "Azul")
        compu4 = Computadora("Lenovo", "ThinkPad", 20000, "8GM", "Gris")
        compu4 = Computadora("HP", "x123", 25000, "12GM", "Roja")

        #Agregan los objetos a la lista
        comput_list.append(compu1)
        comput_list.append(compu2)
        comput_list.append(compu3)
        comput_list.append(compu4)

        menuP = 0
        while menuP != 6:
            print("\n-----Menu Principal-----\n")
            print("1. Agregar una computadora")
            print("2. Mostrar todas las computadoras")
            print("3. Modificar una computadora")
            print("4. Buscar una computadora")
            print("5. Eliminar una computadora")
            print("6. Salir\n")
            
            #Pedimos la opcion con el usuario
            menuP = int(input("Seleccione una opción: "))

            if menuP == 1:
                marca = input("Ingresa la marca de la computadora:")
                modelo = input("Ingresa el modelo de la computadora:")
                precio = float(input("Ingresa el precio de la computadora:"))
                ram = input("Ingresa la Ram de la computadora:")
                color = input("Ingresa el color de la computadora:")

                #Crear el objeto de la nueva computadora
                new_compu = Computadora(marca, modelo, precio, ram, color)
                comput_list.append(new_compu) #Agregamos a la lista
                print("La computadora", new_compu, "Se ha agregado correctamente")

            elif menuP == 2:
                print("-----Lista de computadoras-----")
                for compu in comput_list:
                    print(compu)

            elif menuP == 3:
                compu_mod = input("\nIngresa la marca de la computadora:\n")
                for compu in comput_list:
                    if compu_mod == compu.marca:
                        print("Computadora encontrada:", compu) #Mostrar la compu encontrada
                        print("¿Que desea modificar?")
                        marca = input("Ingresa la nueva marca de la computadora:")
                        modelo = input("Ingresa el nuevo modelo de la computadora:")
                        precio= float(input("Ingresa el nuevo precio de la cmputadora:"))
                        ram = input("Ingresa la nueva RAM de la computadora:")
                        color = input("Ingresa el nuevo color de la computadora:")

                        #Crear el nuevo objeto para meter los datos nuevos
                        compu_mod = Computadora(marca, modelo, precio, ram, color)

                        #Ahora tenemos que quitar la compu vieja y meter la nueva 
                        comput_list[comput_list.index(compu)] = compu_mod
                        print("La computadora se ha modificado correctamente")

            elif menuP == 4:
                print("\n-----Buscar una computadora-----\n")
                compu_busc = input("Ingresa la marca de la computadora que deseas buscar:")

                #Buscarmos y almacenamos
                compu = comput_list[compu_busc]

                print("Computadora encontrada:", compu)

            elif menuP == 5:
                print("\n-----Eliminar una computadora-----\n")
                compu= input("Ingresa la marca de la computadora que deseas eliminar:")

                aux = comput_list[comput_list.index(compu)].marca #Almacenamos la marca para el mensaje

                del comput_list[comput_list.index(compu)] #Eliminamos la compu de la lista
                print("\nLa computadora", aux, "se ha eliminado correctamente\n")

            elif menuP == 6:
                print("Saliendo del programa..")
            else:
                print("Opcion no valida, intente de nuevo")


#Contruimos y ejecutamos el main
if __name__ == "__main__":
    Principal.main()



