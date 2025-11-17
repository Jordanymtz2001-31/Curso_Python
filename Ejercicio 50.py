"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre 
por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el 
nombre del mes.
"""
while True:
    
    print("\nBIENVENIDO AL PROGRAMA DE FECHAS")
    try:
        res = str(input("¿Desea ingresar una fecha? (si/no): ")).lower()
        if res == "no":
            print("Gracias por usar el programa")
            break
        elif res != "si" and res != "no":
            print("Respuesta no valida. Por favor ingrese 'si' o 'no'.\n")
        elif res == "si":
            fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
            dia, mes, anio = fecha.split("/")
            dic = {
                "dia": dia,
                "mes": mes,
                "anio": anio
            }
            print(f"Día {dic['dia']} del Mes {dic['mes']} del Año {dic['anio']}\n")
    except ValueError:
        print("Error: Formato de fecha incorrecto o datos no numéricos. Por favor, use el formato dd/mm/aaaa.\n")
    except IndexError:
        print("Error: Faltan datos en la fecha. Por favor, ingrese día, mes y año.\n")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}\n")