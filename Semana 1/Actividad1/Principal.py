from Usuarios import Usuarios

class Principal:
    def main():

        #Crear la lista de usuarios
        usuarios_list = []

        usuario1 = Usuarios("Jordany", "Martinez", 24, 2331086911, "Masculino")
        usuario2 = Usuarios("Ana", "Gonzalez", 22, 2331086912, "Femenino")
        usuario3 = Usuarios("Luis", "Hernandez", 23, 2331056913, "Masculino")
        usuario4 = Usuarios("Maria", "Lopez", 21, 2331099641, "Femenino")
        usuario5 = Usuarios("Carlos", "Ramirez", 25, 2331089782, "Masculino")

        #Agregamos los usuarios a la lista
        usuarios_list.append(usuario1)
        usuarios_list.append(usuario2)
        usuarios_list.append(usuario3)
        usuarios_list.append(usuario4)
        usuarios_list.append(usuario5)

#Creamos el menu principal
        menuP = 0
        while menuP != 7:
            print("\n-----Menu Principal-----\n")
            print("1.Agregar un usuario")
            print("2.Mostrar todos los usuarios")
            print("3.Buscar un usuario por indice")
            print("4.Buscar un usuario por cadena")
            print("5.Editar un usuario")
            print("6.Eliminar usuario")
            print("7.Salir\n")

            #Pedimos la opcion con el usuario
            menuP = int(input("Selecione una opcion por favor: "))

            if menuP == 1: 
                nombre = input("Ingresa el nombre del usuario:")
                apellido = input("Ingresa el apellido del usuario:")
                edad = int(input("Ingresa tu edad: "))
                numero = int(input("Ingresa tu numero telefonico: "))
                sexo = input("Ingresa tu sexo (Masculino/Femenino): ")

                #Crearmos el nuevo usuario o nuevo onjeto
                new_usuario = Usuarios(nombre, apellido, edad, numero, sexo)
                usuarios_list.append(new_usuario) #Agregamos a la lista
                print("El Usuario", {new_usuario}, "Se ha agregado exitosamente")

            elif menuP == 2:
                print("-----Lista de Usuarios-----")
                for usuario in usuarios_list:
                    print(usuario)
            
            elif menuP == 3:
                print("\n-----Buscar un usuario por indice-----\n")
                indice = int(input("Ingresa el indice del usuario que deseas buscar: ")) 
                if 0 <= indice < len(usuarios_list):
                    usuario = usuarios_list[indice -1]
                    print("Usuario:", usuario)
                else:
                    print("Indice fuera de rango. Ranggo valido: 0..")

            elif menuP == 4:
                print("\n-----Buscar un usuarios por cadena-----\n")
                cadena = input("Ingresa el nombre del usuario que deseas buscar: ")
                for usuario in usuarios_list:
                    if cadena == usuario.nombre:
                        print("Usuario encontrado:",f"{usuario}")
                        break
                else:
                    print("Usuario no encontrado")


            elif menuP == 5:
                print("\n-----Editar un usuario en dos campos-----\n")
                buscar_nombre = input("Ingresa el usuario que deseas editar: ").strip() #El strip elimina espacios en blanco que existan
                
                if not buscar_nombre:
                        print("No se ingreso ningun nombre")
                        continue #El continue hace que se regrese al inicio del ciclo
                
                #Buscar el usuario por nombre
                usuario_encontrado = None
                for usuario in usuarios_list:
                        #Con getattr accede al altributo que queremos del objeto
                        if getattr(usuario, "nombre", "").lower() == buscar_nombre.lower():
                            usuario_encontrado = usuario
                            break #Sale del ciclo for
                if usuario_encontrado is None:
                        print(f"Usuario no encontrado, {buscar_nombre} ")
                        continue
                print("Usuario encontrado:", usuario_encontrado)

                #Creamos un diccionario
                
                campos = {
                    "1": ("nombre", "Nombre"),
                    "2": ("apellido", "Apellido"),
                    "3": ("edad", "Edad"),
                    "4": ("numero", "Número telefónico"),
                    "5": ("sexo", "Sexo")
                        }
                
                #Mostrar opciones
                #Aqui el k es es el campo clave y lo que es (_ este se ignora, label es el valor de la lista)
                print("\nElige exactamente Dos campos (Eliga los numero uno por uno")
                for k, (_, label) in campos.items(): 
                    print(f"{k}. {label}") 

                Seleccion1 = input("Primera Opcion: ").strip()
                Seleccion2 = input("Segunda Opcion: ").strip()

                if Seleccion1 == Seleccion2:
                    print("Las dos opciones debeb de ser diferentes")
                    continue
                if Seleccion1 not in campos or Seleccion2 not in campos:
                    print("Opcione Invalida. Debes de colocar opciones del 1-5")
                    continue
                
                elecciones = [campos[Seleccion1][0], campos[Seleccion2][0]] #Nombre de los atributos

                #Pedimos los valores seleccionados 
                for attr in elecciones:
                    if attr == "nombre":
                        n_nombre = input("Coloca el  nuevo nombre: ").strip()
                        setattr(usuario_encontrado, "nombre", n_nombre)
                    elif attr == "apellido":
                        n_apellido = input("Coloca el nuevo apellido: ").strip()
                        setattr(usuario_encontrado, "apellido", n_apellido)
                    elif attr == "edad":
                        try:
                            n_edad = int(input("Coloca la nueva edad: ").strip())
                            setattr(usuario_encontrado, "edad", n_edad)
                        except ValueError:
                            print("Edad Invalida, debe de ser un numero entero")
                            continue
                    elif attr == "numero":
                        try:
                            n_numero = int(input("Coloca el nuevo número telefónico: ").strip())
                            setattr(usuario_encontrado, "numero", n_numero)
                        except ValueError:
                            print("Número telefónico Invalido, debe de ser un numero entero")
                            continue
                    elif attr == "sexo":
                        n_sexo = input("Coloca el nuevo sexo: ").strip()
                        setattr(usuario_encontrado, "sexo", n_sexo)
                print("Usuario Actualizado exitosamente:", usuario_encontrado)

            elif menuP == 6: 
                print("\n-----Eliminar un usuario-----\n")
                
                #Validar el idice
                if len(usuarios_list) == 0:
                    print("No hay usuarios para eliminar")
                    continue
                #Solicitar el índice del usuario a eliminar
                indice = int(input("Ingresa el índice del usuario que deseas eliminar (1,2,3,4,5): "))
        
                #Validar el índice
                indice -= 1 #Ajustar que el usuario ingrese 1..n
                if indice < 0 or indice >= len(usuarios_list):
                    print("Índice inválido")
                    continue
                #Eliminar el usuario
                aux = usuarios_list[indice].nombre #Almacenamos el nombre que se elimina
                usuarios_list.pop(indice) #Elminamos el usuario de la lista
                print(f"El usuario {aux} se ha eliminado correctamente")

            elif menuP == 7:
                print("Saliendo del programa..")
            else:
                print("Opcion no valida, intente de nuevo")

#Contruimos y ejecutamos el main
if __name__ == "__main__":
    Principal.main()
