class Refaccionaria:
    def __init__(self, nombre, ubicacion, tipo_refaccionaria, precio_refaccion, stock, precio_compra):
        self._nombre = nombre
        self._tipo_refaccionaria = tipo_refaccionaria
        self._ubicacion = ubicacion
        self._precio_refaccion = precio_refaccion
        self._stock = stock
        self._precio_compra = precio_compra
        self._ganacia = precio_refaccion - precio_compra

    def __str__(self):
        return (f"{self._nombre}",
                f"{self._tipo_refaccionaria}",
                f"{self._ubicacion}",   
                f"{self._precio_refaccion}",
                f"{self._stock}",
                f"{self._precio_compra}",
                f"{self._ganacia}")
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def tipo_refaccionaria(self):
        return self._tipo_refaccionaria
    
    @tipo_refaccionaria.setter
    def tipo_refaccionaria(self, nuevo_tipo):
        self._tipo_refaccionaria = nuevo_tipo

    @property
    def ubicacion(self):
        return self._ubicacion
    
    @ubicacion.setter
    def ubicacion(self, nueva_ubi):
        self._ubicacion = nueva_ubi

    @property
    def precio_refaccion(self):
        return self._precio_refaccion
    
    @precio_refaccion.setter
    def precio_refaccion(self, nuevo_precio):
        self._precio_refaccion = nuevo_precio
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, nuevo_stock):
        self._stock = nuevo_stock
    
    @property
    def precio_compra(self):
        return self._precio_compra
    
    @precio_compra.setter
    def precio_compra(self, nuevo_precio_compra):
        self._precio_compra = nuevo_precio_compra

    @property 
    def ganancia (self):
        return self._ganacia
    
    @ganancia.setter
    def ganancia(self, nueva_ganancia):
        self._ganacia = nueva_ganancia
    
