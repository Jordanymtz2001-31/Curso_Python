abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def eliminar_letras(abc):
    letras_restantes = []
    for letra  in range(len(abc)):
        if letra % 3 != 0:
            # append es para agregar un elemento al final de la lista
            # pop es para eliminar un elemento de la lista
            letras_restantes.append(abc[letra - 1])

    return f"Las letras restantes son: {letras_restantes}"

print(eliminar_letras(abc)) 