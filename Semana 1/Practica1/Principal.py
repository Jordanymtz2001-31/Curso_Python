from Autos import Autos

#Instancia de la clase Autos
auto1 = Autos("Toyota", "Corolla", 2020, "Rojo")
auto2 = Autos("Chevrolet", "Malibu", 2021, "Azul")

print(auto1) #LLama al metodo __str__
print("----------------------------------------")


#Modificar 
auto1.set_marca("Honda")
print(auto1)
print("----------------------------------------")

#Obtener informacion
print("Marca del Auto1: \n" + auto1.get_marca()+
      "\nModelo del Auto1: \n" + auto1.get_modelo()+
        "\nAño del Auto1: \n" + str(auto1.get_año())+
            "\nColor del Auto1: \n" + auto1.get_color()+
            "\n ---------------------------------------")

#Obtener informacion con f-string
print(f"Marca del Auto1: \n{auto1.get_marca()}"
      f"\nModelo del Auto1: \n{auto1.get_modelo()}"
      f"\nAño del Auto1: \n{auto1.get_año()}"
      f"\nColor del Auto1: \n{auto1.get_color()}")
print("----------------------------------------")

print(Autos.mostrar_cantidad()) #Llamamos al metodo de clase para mostrar