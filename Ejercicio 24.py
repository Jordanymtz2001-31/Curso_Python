palabra = input("Ingrese una palabra: ")

#Palabra repetida 10 veces en filas
def repetir_palabra(palabra):
    if palabra == "":
        return "No se ingreso ninguna palabra"
    else:
        #Imprimimos 10 veces la palabra por fila
        for i in range(10): # i es 
            print(palabra)

print(repetir_palabra(palabra))