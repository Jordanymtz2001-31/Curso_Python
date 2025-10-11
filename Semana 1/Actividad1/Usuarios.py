class Usuarios:
    def __init__(self, nombre, apellido, edad, numero, sexo):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._numero = numero
        self._sexo = sexo

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido} {self.edad} {self.numero} {self.sexo}"
    
    @property #Getter
    def nombre(self):
        return self._nombre
    
    @nombre.setter #Settter
    def nombre(self, new_nombre):
        self._nombre = new_nombre

    @property #Getter
    def apellido(self):
        return self._apellido
    
    @apellido.setter #Settter
    def apellido(self, new_apellido):
        self._apellido = new_apellido

    @property #Getter
    def edad(self):
        return self._edad
    
    @edad.setter #Settter
    def edad(self, new_edad):
        self._edad = new_edad

    @property #Getter
    def numero(self):
        return self._numero
    
    @numero.setter #Settter
    def numero(self, new_numero):
        self._numero = new_numero

    @property #Getter
    def sexo(self):
        return self._sexo
    
    @sexo.setter #Settter
    def sexo(self, new_sexo):
        self._sexo = new_sexo



        