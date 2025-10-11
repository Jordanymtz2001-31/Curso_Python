try:
    numero = int(input("Introduce un número para elevarlo al cuadrado: "))
    print(f"El cuadrado del número es: {numero ** numero}")

    #División por cero
    x = 5 / numero

    #El type error ocurre cuando se intenta operar con tipos de datos incorrectos
    #El value error ocurre cuando se intenta convertir un string a un entero y el string no es un número
    #El exception es una excepción genérica que captura cualquier error no previsto
    #El ZeroDivisionError ocurre cuando se intenta dividir un número entre cero
except TypeError:
    print("\nDebes convertir tus cadenas a enteros desde el input")
except ZeroDivisionError:
    print("\nNo se puede dividir entre cero")
except ValueError:
    print("\nIntroduce un número entero correcto")
except Exception as e:
    print(f"\nHa ocurrido un error no previsto: {e}")
else:
    print("\nNo ha habido ningún error")
finally:
    print("\nGracias por usar este programa")

    #El else se ejecuta si no hay ningún error
    #El finally se ejecuta siempre, haya o no errores