

num1 = int(input("Dame el primero numero: "))
num2 = int(input("Dame el segunfo numero: "))

def buscar_dividendo(num1, num2):
    if num1 == 0 or num2 == 0:
        return "No se puede dividir entre 0"
    
    if num1 > num2:
        divicion = num1 / num2
        resto =  num1 % num2
    else :
        divicion = num2 /num1
        resto = num2 % num1 
    
    return f"El resultado es: {divicion} y el resto es: {resto} "



print ("El resultado: ", buscar_dividendo(num1,num2))
