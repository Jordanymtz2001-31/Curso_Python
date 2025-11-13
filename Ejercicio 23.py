pizza = input("¿Que pizza deseas?(Vegetariana/No Vegetariana):").lower() #El strip es para eliminar espacios en blanco

def ingredientes(pizza):
    if pizza == "":
        return "No se ingreso nungun valor"
    elif pizza == "vegetariana":
        ingredientes_veg = ["Pimiento", "Tofu"]
        print(f"Ingredientes para pizza vegetariana: {', '.join(ingredientes_veg)}") #El .join es para unir los elementos de la lista en una cadena separada por comas
        elegir = input("Elige solo uno de los ingredientes adicionales (Pimiento/Tofu): ").strip().lower()
        #SI eligo dos no puedo hacer eso
        if elegir == "pimiento" and elegir == "tofu":
            return "Solo puedes elegir un ingrediente adicional"
        if elegir in ["pimiento", "tofu"]:
            return (f"Has elegido {elegir} como ingrediente adicional junto con mozzarella y el tomate ")
    elif pizza == "no vegetariana":
        ingredientes_no_veg = ["Pepperoni", "Jamón", "Queso"]
        print(f"Ingredientes para pizza no vegetariana: {', '.join(ingredientes_no_veg)}\n") #El .join es para unir los elementos de la lista en una cadena separada por comas
        elegir = input("Elige solo uno de los ingredientes adicionales (Pepperoni/Jamón/Queso): ").strip().lower()
        if elegir == "pepperoni" and elegir == "jamón" and elegir == "queso":
            return "Solo puedes elegir un ingrediente adicional"
        if elegir in ["pepperoni", "jamón", "queso"]:
            return (f"Has elegido {elegir} como ingrediente adicional junto con mozzarella y el tomate ")
    else:
        return "Tipo de pizza no reconocido"

print(ingredientes(pizza))