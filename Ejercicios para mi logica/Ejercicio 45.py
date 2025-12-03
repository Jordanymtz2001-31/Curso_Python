vectores1 = (1,2,3)
vectores2 = (-1,0,2)

def poducto_escalar(vectores1, vectores2):
    producto = 0
    for i in range(len(vectores1)):
        producto += vectores1[i] * vectores2[i]
    return producto

print(poducto_escalar(vectores1, vectores2))