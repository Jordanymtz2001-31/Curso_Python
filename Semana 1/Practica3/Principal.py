from Refaccionaria import Refaccionaria

def main():

    #Creamos lista
    lista = []

    #instanciamos objetos
    refac1 = Refaccionaria("Refaccionaria El Clavo", "Av. Siempre Viva 123", "LLantas", 150.0, 10, 100.0)
    refac2 = Refaccionaria("Refaccionaria La Tuerca", "Calle Falsa 456", "Mangueras", 80.0, 10, 50.0)
    refac3 = Refaccionaria("Refaccionaria El Tornillo", "Boulevard Central 789", "Frenos", 40.0, 10, 25.0)
    refac4 = Refaccionaria("Refaccionaria la Rueda", "Plaza Mayor 101", "Volante", 200.0, 10, 120.0)
    refac5 = Refaccionaria("Refaccioanria El Motor", "Av. Libertad 202", "Balatas", 90.0, 10 , 60.0)

    #Guardamos los objetos
    #Con el extend podemos guardarlos todos en una sola linea
    lista.extend([refac1, refac2, refac3, refac4, refac5])

    while True:
        print("\n--- Menu de Opciones ---")
        print("1.Ingresar por nombre")
        print("2.Editar por nombre")
        print("3.Eliminar por nombre")
        print("4.Buscar por nombre o ubicacion")
        print("5.Comprar refaccion")
        print("6.Imprimir")
        print("7.Salir")

        opcion = input("Seleccione una opción (1-7): ")

        #Validados que la opcion sea correcta
        #Con isdigit es devolver verdadero si son valores entero y falso si hay espacio y numero/caracteres
        if not opcion.isdigit() or not (1 <= int(opcion) <=8):
            print("Opción inválida. Por favor, seleccione una opción del 1 al 7.")
            continue #continue nos regresa al inicio del while

        opcion = int(opcion) #Convertimos la opcion a entero

        if opcion == 1: 
            print("\nRegistrar una nueva refaccion: ")
            nombre = input("Nombre de la refaccion: ")


            #Verificamos que el nombre no exista
            #Any verificar si al menos un elemento de un iterable (lista, tupla, conjunto, etc.) es verdadero (True).
            #El for recorrera cada elemneto de la lista para verificar
            if any(r.nombre.lower() == nombre.lower() for r in lista):
             print("Error: Ya existe este nombre, intenta con otro")
            else:
                #Pedimos los demas datos
                ubicacion = input("Ubicacion: ")
                tipo_refaccionaria = input("Tipo de refaccionaria: ")
                precio_refaccion = float(input("Precio de refaccion: "))
                stock = int(input("Stock: "))
                precio_comprar = float(input("Precio de comprar: "))
            
                #Creamos el objeto
                refaccionaria_new = Refaccionaria(nombre, ubicacion, tipo_refaccionaria, precio_refaccion, stock, precio_comprar )
                lista.append(refaccionaria_new) #Agregamos el objeto a la lista
                print("Refaccion registrada exitosamente")
            
        elif opcion == 2:
            print("\n Editar una refaccion por nombre")
            nombre = input("Nombre de la refaccion que quiere modificar: ")
            
            #Variable que no tienen ningun valos aun
            refac_encontrada = None

            for r in lista:
                if r.nombre.lower() == nombre.lower():
                    refac_encontrada = r
                    break

            if refac_encontrada:
                print("Refaccionaria encontrada, ingresa los nuevos valores:")

                try:

                    refac_encontrada.nombre = input("Nombre: ").strip()
                    refac_encontrada.ubicacion = input("Ubicacion: ").strip()
                    refac_encontrada.tipo_refaccionaria = input("Tipo de refaccionaria: ").strip()
                    refac_encontrada.precio_refaccion = float(input("Precio de refaccion: "))
                    refac_encontrada.stock = int(input("Stock: "))
                    refac_encontrada.precio_comprar = float(input("Precio de comprar: "))
                    refac_encontrada.ganancia = refac_encontrada.precio_refaccion - refac_encontrada.precio_comprar
                    print("Refaccionaria actualizada exitosamente")

                except ValueError:
                    print("Error: alguno de los valores numericos no es valido" )
                
                else: 
                    #Actualizar la ganacia
                    refac_encontrada.ganancia = refac_encontrada.precio - refac_encontrada.precio_comprar
                    print("Refaccionaria actualizada exitosamente")

            else:
                print("Refaccionaria no encontrada")
            
        elif opcion == 3:
            print("\n Eliminar una refaccion por nombre")
            nombre = input("Nombre de la refaccion a eliminar: ")
            refac_encontrada = False

            for i in range(len(lista)):
                if lista[i].nombre.lower() == nombre.lower(): #El lower ignora mayusculas y minusculas
                    lista.pop(i) #El pop elimina el elemento en el indice especificado
                    refac_encontrada = True
                    print("Refaccionaria eliminada exitosamente")
                    break
            if not refac_encontrada:
                print("Refaccionaria no encontrada")

        elif opcion == 4:
            print("\n Buscar por nombre o ubicacion")

            consulta = input("Ingresa el nombre o ubicacion a buscar: ")

            encontrado = False

            for r in lista: 
                if r.nombre.lower() == consulta.lower() or r.ubicacion.lower() == consulta.lower():
                    print("Nombre: " + str(r.nombre))
                    print("Ubicacion: " + str(r.ubicacion))
                    print("Tipo de refaccionaria: " + str(r.tipo_refaccionaria))
                    print("Precio de refaccion: " + str(r.precio_refaccion))
                    print("Stock: " + str(r.stock))
                    print("Precio de comprar:" + str(r.precio_compra))
                    encontrado = True

            if not encontrado:
                print("No se encontraron resultados.")
            
        elif opcion == 5:
            print("\n Comprar refaccion")

            #Creamos una lista de refacciones
            tipos_refacciones = []
            for r in lista:    #Iteramos sobre la lista de refaccionarias
                if r.tipo_refaccionaria not in tipos_refacciones: #Verificamos que el tipo no exista en la lista
                    tipos_refacciones.append(r.tipo_refaccionaria) #Agregamos el tipo de refaccionaria a la lista si no existe
                    print(f"{tipos_refacciones.index(r.tipo_refaccionaria) + 1}. - {r.tipo_refaccionaria}") #Imprimimos el tipo de refaccionaria con su indice
                    
            if not tipos_refacciones:
                print("No hay refaccionarias disponibles")
                continue

            #Mostrar un contador automatico de las refacciones disponibles
            for inx, tipo in enumerate(tipos_refacciones, start=1):
                print(f"{inx}.-{tipo}")


            opcion_tipo = int(input("Selecciona el indice de la refaccion que desea comprar: "))
            #Validamos que la opcion este dentro del rango
            if opcion_tipo < 1 or opcion_tipo > len(tipos_refacciones):
                print("Opcion Invalida")
                continue
                
            #Validamos que la opcion este dentro del rango
            if opcion_tipo < 1 or opcion_tipo > len(tipos_refacciones):
                print("Opcion Invalida, esta fuera de las opciones")
                continue

            tipo_selecionado = tipos_refacciones[opcion_tipo - 1] #Obtenemos el tipo de refaccionaria selecionado

            #Con next buscamos en la lista el primer elemento que cumpla con la condicion
            refaccionaria_selecionada = next((r for r in lista if r.tipo_refaccionaria == tipo_selecionado), None ) #Obtenemos la refaccionaria selecionada
            if refaccionaria_selecionada is None:
                print("Error inesperado: no se encontro la refaccionaria")
                continue

            print(f"Cantidad disponible en stock: {refaccionaria_selecionada.stock}")
            print(f"Precio de la refaccion: ${refaccionaria_selecionada.precio_refaccion}")

            #Leer cantidad a compar y validar
            try:
                cantidad_comprada = int(input("Ingresa la cantidad que desea comprar: ").strip())
            except ValueError:
                print("Cantidad Invalida. Debes ingresar numero enteros")
                continue



            if cantidad_comprada > refaccionaria_selecionada.stock or cantidad_comprada <= 0:
                print("No hay suficiente stock disponible.")
                continue
                
            #Calcular totales y actualizar stock
            total_pagar = cantidad_comprada * refaccionaria_selecionada.precio_refaccion
            nuevo_stock = refaccionaria_selecionada.stock - cantidad_comprada
            refaccionaria_selecionada.stock = nuevo_stock
            ganancia_refac = cantidad_comprada * refaccionaria_selecionada.ganancia

            print(f"\nTotal a pagar: ${total_pagar}")
            print(f"Ganancia obtenida por esta compra: ${ganancia_refac}")

        elif opcion == 6:
            print("\nOpcion para imprimir las refaccionarias\n")
            for refac in lista:
                print(f"Nombre: {refac.nombre}")
                print(f"Ubicacion: {refac.ubicacion}")
                print(f"Tipo de Refaccion: {refac.tipo_refaccionaria}")
                print(f"Stock: {refac.stock}")
                print(f"Ganancia: {refac.ganancia}")
                print("--------------------------")

        elif opcion == 7:
            print("Saliendo del programa")
            break #Sale del bucle infitino
    
if __name__ == "__main__":
    main()
