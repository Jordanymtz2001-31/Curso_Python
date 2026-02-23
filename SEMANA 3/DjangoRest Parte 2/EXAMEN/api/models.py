from django.db import models, transaction
from decimal import Decimal

class Denominacion(models.Model):
    TIPO_CHOICES = [
        ('billete', 'Billete'), ('moneda', 'Moneda')
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.tipo.capitalize()} ${self.valor}"
    
    @classmethod #Definimos un método de clase
    def inicializar_cajero(cls):
        """Inicializa el cajero con $12,550 MXN diarios"""
        with transaction.atomic(): # Utilizamos la función atomic para manejar la transacción
            cls.objects.all().delete()
            denominaciones = [
                ('billete', Decimal('1000'), 2),
                ('billete', Decimal('500'), 5),
                ('billete', Decimal('200'), 10),
                ('billete', Decimal('100'), 20),
                ('billete', Decimal('50'), 30),
                ('moneda', Decimal('20'), 40),
                ('moneda', Decimal('10'), 50),
                ('moneda', Decimal('5'), 100),
                ('moneda', Decimal('2'), 200),
                ('moneda', Decimal('1'), 300),
                ('moneda', Decimal('0.50'), 100),
            ]

            #Para sacar el total de lo que tiene el cajero
            #Primero vamos a sumar todo lo que tiene la lista de duplas
            #Luego vamos a multiplicar el valor de cada dupla por la cantidad
            #Pero ignoramos con _ el primer elemento de la dupla
            total = sum(valor * cantidad for _, valor, cantidad in denominaciones)

            #Ahora vamos a recorrer la lista de duplas y vamos a crear los objetos
            for tipo, valor, cantidad in denominaciones:
                cls.objects.create(tipo=tipo, valor=valor, cantidad=cantidad)
            return {'mensaje': f'Cajero inicializado con ${total} MXN'}
        


