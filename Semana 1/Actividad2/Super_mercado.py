class Productos:

    def __init__(self, nombre, precio, categoria, stock, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.descripcion = descripcion

    def __str__(self):
        return f"El producto es: {self.nombre}, {self.precio}, {self.categoria}, {self.descripcion}, {self.stock} "
        
    #Set y getter
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, new_nombre):
        self.nombre = new_nombre

    def get_precio(self):
        return self.precio
    
    def set_precio(self, new_precio):
        self.precio = new_precio
    
    def get_categoria(self):
        return self.categoria
    
    def set_categoria(self, new_categoria):
        self.categoria = new_categoria

    def get_stock(self):
        return self.stock
    
    def set_stock(self, new_stock):
        self.stock = new_stock

    def get_descripcion(self):
        return self.descripcion
    
    def set_descripcion(self, new_descripcion):
        self.descripcion = new_descripcion


class Cliente:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return (f"Usuario: {self.nombre}" )
    
    