from Super_mercado import Productos
from Super_mercado import Cliente

class Principal:

    def __init__(self):
        
        
        #Creamos lista
        self.Products_list = []

        #Creamos instancias
        producto1 = Productos("Gelletas", 20, "Panaderia", 10, "Chocolate")
        producto2 = Productos("Doritos", 20, "Chatarra", 10, "Nachos")
        producto3 = Productos("Agua", 15, "Bebidas", 10, "Ciel")
        producto4 = Productos("Papel", 25, "Cuidados del hogas",10, "Bogue")
        producto5 = Productos("Leche", 30, "Bebidas", 10, "Alpura")

        #Guardamos
        self.Products_list.extend([producto1, producto2, producto3, producto4, producto5])
    def menu(self):
        nombre_usuario = input("Ingresa tu nombre: ")
        while not nombre_usuario:
            print("Nombre no valido. Intente de nuevo")
            nombre_usuario = input("Ingresa de nuevo tu nombre: ").strip()
        # Guardar el nombre en la instancia para usarlo en otros métodos
        self.nombre_usuario = nombre_usuario
        #Si esta bien su nombre damos la bienvenida
        print(f"\nBienvenido al menu,{nombre_usuario}!")

        while True:
            print("\n--- Menu de Opciones ---")
            print("1.- Ingresar Productos: ")
            print("2.- Lista de productos existente: ")
            print("3.- Buscamos prodcutos por indice: ")
            print("4.- Editamos prodcutos por indice: ")
            print("5.- Eliminamos prodcutos por indice: ")
            print("6.- Comprar Prodcutos :")
            print("7.- Salir")

            opcion = input("Seleccione una opción (1-7): ")

            match opcion:
                case "1":
                    self.ingresar_prodcutos()
                case "2":
                    self.lista_prodcutos()
                case "3":
                    self.buscar_prodcutos()
                case "4":
                    self.editar_prodcutos()
                case "5":
                    self.eliminar_prodcutos()
                case "6":
                    self.compar_productos()
                case "7":
                    print("Saliendo del programa")
                    break
                case _:
                    print("Opcion invalidad, intente de nuevo")
                
    def ingresar_prodcutos(self):
        #Pedimos los datos
        nombre = input("Nombre del nuevo producto: ")
        precio = int(input("Ingresa el precio: "))
        categoria = input("Categoria del producto: ")
        stock = int(input("Cantidad que deseas meter: "))
        descripcion = input("Breve descripcion: ")

        #Cremamos el objeto
        Nuevo_producto = Productos(nombre, precio, categoria, stock, descripcion)
        #Agregamos a la lista
        self.Products_list.append(Nuevo_producto)
        print("Producto registrado correctamente")

    def lista_prodcutos(self):
        if len(self.Products_list) == 0:
            print("No hay productos disponibles")
        else:
            for i, productos in enumerate(self.Products_list):
                print(f"{i}.-{productos}")

    def buscar_prodcutos(self):
        indide_product = int(input("Ingresa el indice del prodcuto que quieres buscar: "))
        print(self.Products_list[indide_product])

    def editar_prodcutos(self):
        indice_product = int(input("Ingresa el indice del producto que desea editar: "))
        product = self.Products_list[indice_product]

        print("\nIngresa los nuevos valores y deja en blando los valores que no quieres cambiar\n")

        #Solicitamos los valores o si no se mete los valores que obtenga el que ya tiene
        nombre = input(f"Nuevo nombre({product.get_nombre()}): ") or product.get_nombre()
        precio = input(f"Nuevo precio({product.get_precio()}): ") or product.get_precio()
        categoria = input(f"Nuevo categoria({product.get_categoria()}): ") or product.get_categoria()
        stock = input(f"Nuevo stock({product.get_stock()}): ") or product.get_stock()
        descripcion = input(f"Nuevo descripcion({product.get_descripcion()}): ") or product.get_descripcion()

        #Metemos los velores a productos
        product.set_nombre(nombre)
        product.set_precio(precio)
        product.set_categoria(categoria)
        product.set_stock(stock)
        product.set_descripcion(descripcion)

        print("\nProducto editado exitosamente\n")

    def eliminar_prodcutos(self):
        indice_product = int(input("Ingresa el indice que deseas eliminar: "))
        self.Products_list.pop(indice_product)
        print("Prodcutos eliminado correctamente")

    def compar_productos(self):
        print("\n--------Comprar Productos--------")
            #Creamos una lista de refacciones
        tipos_productos = []
        for r in self.Products_list:    #Iteramos sobre la lista de refaccionarias
            if r.nombre not in tipos_productos: #Verificamos que el el nombre no exista en la lista
                tipos_productos.append(r.nombre) #Agregamos el tipo de refaccionaria a la lista si no existe
                #print(f"{tipos_productos.index(r.nombre) + 1}. - {r.nombre}") #Imprimimos el nombre con su indice
                    
        if not tipos_productos:
            print("No hay productos disponibles")
            return

        #Mostrar un contador automatico de las refacciones disponibles
        for inx, nombre in enumerate(tipos_productos, start=1):
             print(f"{inx}.-{nombre}")


        opcion_product = int(input("Selecciona el producto que desea comprar: "))
        #Validamos que la opcion este dentro del rango
        if opcion_product < 1 or opcion_product > len(tipos_productos):
            print("Opcion Invalida")
            return

        product_selecionado = tipos_productos[opcion_product - 1] #Obtenemos el tipo de refaccionaria selecionado

        #Con next buscamos en la lista el primer elemento que cumpla con la condicion
        product_selecionado = next((r for r in self.Products_list if r.nombre == product_selecionado), None ) #Obtenemos la refaccionaria selecionada
        if product_selecionado is None:
            print("Error inesperado: no se encontro el producto")
            return

        print(f"Cantidad disponible en stock: {product_selecionado.stock}")
        print(f"Precio de la refaccion: ${product_selecionado.precio}")

        #Leer cantidad a compar y validar
        try:
                cantidad_comprada = int(input("Ingresa la cantidad que desea comprar: ").strip())
        except ValueError:
            print("Cantidad Invalida. Debes ingresar numero enteros")
            return



        if cantidad_comprada > product_selecionado.stock or cantidad_comprada <= 0:
            print("No hay suficiente stock disponible.")
            return
                
        #Calcular totales y actualizar stock
        total_pagar = cantidad_comprada * product_selecionado.precio
        nuevo_stock = product_selecionado.stock - cantidad_comprada
        product_selecionado.stock = nuevo_stock

        # Construir items comprados (aquí solo 1 producto)
        items = [{
            'Nombre': getattr(product_selecionado, 'nombre', product_selecionado.get_nombre()),
            'Precio_Unidad': float(getattr(product_selecionado, 'precio', product_selecionado.get_precio())),
            'Cantidad': int(cantidad_comprada)
        }]

        #Imprimimos el cliente
        print(f"\nCliente: {self.nombre_usuario}\n")

        # Cabecera (ajusta los anchos si quieres)
        print(f"{'Producto':<12} {'Precio':>12} {'Cantidad':>10} {'Subtotal':>12}")
        print("-" * 50)

        total = 0.0
        for it in items: #Ocupamos la lista items y usamos el for para iterar 
            nombre = it['Nombre']
            unidad = it['Precio_Unidad']
            cantidad = it['Cantidad']
            subtotal = unidad * cantidad
            total += subtotal
            # imprime: nombre (izq), precio (der), cantidad (der), subtotal (der)
            print(f"{nombre:<12} {unidad:12.0f} {cantidad:10d} {subtotal:12.0f}\n")

        print(f"Total : ${total:.2f}\n")
    


if __name__ == "__main__":
    app = Principal() #Creamos una instancia
    app.menu() #Llamamos a la funcion
    