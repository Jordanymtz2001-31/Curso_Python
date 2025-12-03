
precios = (50, 75, 46, 22, 80, 65, 8)

def precios_mayor_manenor (precios):            
        for n in precios:
                for m in precios:
                        if n > m:
                                mayor = n
                        if n < m:
                                menor = n
        return f"El precio mayor es {mayor} y el precio menor es {menor}"
        
print(precios_mayor_manenor(precios))