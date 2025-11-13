from django.shortcuts import render, get_object_or_404, redirect
from .models import Mascotas

# Create your views here.
def listar_mascotas(request):
    mascotas = Mascotas.objects.all() #Recupere toda la informacion de la bd
    #Renderiza la lista de mascotas en la plantilla html
    return render(request, "listar_mascotas.html", {"mascotas": mascotas})

def guardar_mascota(request):
    #Verificamos que la peticion sea POST
    if request.method == "POST":
        #Obtenemos los valores del formulario
        v_nombre = request.POST.get("nombre")
        tipo = request.POST.get("tipo")
        edad = request.POST.get("edad")
        categoria = request.POST.get("categoria")
        
        if v_nombre and tipo and edad and categoria:
            #Creamos la nueva mascota
            Mascotas.objects.create(
                nombre = v_nombre,
                tipo = tipo,
                edad = edad,
                categoria = categoria
            )
            #Redirige al usuario a la lista de mascotas actualizada
            return redirect("listar_mascotas_url")
    #Si no es POST, entonces renderiza la plantilla para guardar 
    return render(request, "guardar_mascota.html")
        
def editar_mascota(request, idMascota):
    #Buscamos la mascota por su id y no la encuentra retornamos un 404
    mascota = get_object_or_404(Mascotas, id = idMascota)
    
    #Validamos que la peticion dea POST
    if request.method == "POST":
        #Actualizamos cada uno de los campos de la "mascota" que encontradmos por los nuevos valores de los input.
        mascota.nombre = request.POST.get("nombre")
        mascota.tipo = request.POST.get("tipo")
        mascota.edad = request.POST.get("edad")
        mascota.categoria = request.POST.get("categoria")
        
        #Guardamos los cambios en la bd
        mascota.save()
        return redirect("listar_mascotas_url")
    
    return render(request, "editar_mascotas.html", {"mascota": mascota})

def eliminar_mascota(request, idMascota):
    mascota = get_object_or_404(Mascotas, id = idMascota)
    mascota.delete() #Eliminamos la mascota
    return redirect("listar_mascotas_url")

def buscar_mascota(request):
    #Obtenemos el nombre desde el formulario
    encontrado = request.GET.get("nombre_buscado", "")
    
    if encontrado:
        #Almacenamos todas las mascotas filtradas por nombre
        mascotas = Mascotas.objects.filter(nombre__icontains = encontrado)
    else:
        mascotas = Mascotas.objects.all()
    #Renderizamos la peticion a la plantilla de busqueda html
    return render(request, "buscar_mascota.html", {"mascotas": mascotas, "encontrado": encontrado})
    
    