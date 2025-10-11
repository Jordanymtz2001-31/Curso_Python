#Exceppciones personalizadas

class SaldoInsuficiente_error(Exception):
    
    def __init__(self, mensaje):
        super().__init__(mensaje)

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a depositar debe ser mayor a 0.")

        self.saldo += cantidad
        print(f"Depósito exitoso de {cantidad}. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        elif cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor a 0.")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso de {cantidad}. Nuevo saldo: {self.saldo}")

    def mostrar_saldo(self):
        print(f"El saldo actual de la cuenta de {self.titular} es: {self.saldo}")


try:
    cuenta = CuentaBancaria("Juan Perez", 1000)
    cuenta.mostrar_saldo()
    
    deposito = float(input("Introduce la cantidad a depositar: "))
    cuenta.depositar(deposito)
    cuenta.mostrar_saldo()

    retiro = float(input("Introduce la cantidad a retirar: "))
    cuenta.retirar(retiro)
    cuenta.mostrar_saldo()

except SaldoInsuficiente_error as sie:
    print(f"Error: Saldo insuficiente. {sie}")

except ValueError as ve:
    print(f"Error: {ve}")

else:
    print("Todo salio bien..")

finally:
    print("Gracias por usar el sistema bancario.")