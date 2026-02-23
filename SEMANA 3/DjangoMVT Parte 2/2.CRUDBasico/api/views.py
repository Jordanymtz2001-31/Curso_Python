from django.shortcuts import get_object_or_404, redirect, render
from api.models import Mascotas
from django.contrib import messages

#Metodo para listas
def listar_mascotas(request):

    #Obtenermos todas las mascotas del modelo Mascotas y las colocamos en la variable 
    mascotas = Mascotas.objects.all()

    #Renderizamos la lista de mascotas en una plantilla
    #Le pasamos la peticion, el nombre de la plantilla y un diccionario (la lista de mascotas)
    return render(request, 'listar_mascotas.html', {'mascotas': mascotas})

def guardar_mascotas(request):

    if request.method == 'POST':

        #Obtenemos los datos del formulario de la plantilla
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
        peso = request.POST.get('peso')
        especie = request.POST.get('especie')

        #Validamos los datos que no esten vacios
        if nombre and edad and peso and especie:
            
            #Creamos una nueva mascota
            Mascotas.objects.create(
                nombre=nombre,
                edad=edad,
                peso=peso,
                especie=especie
            )

            #Mostramos un mensaje de exito
            messages.success(request, 'Mascota creada exitosamente')
            #Redirigimos al usuario a la lista de mascotas
            return redirect('listar_mascotas_url') #Con redirect Asemos la accion mas ir al otro lado

        else:
            #Mostramos un mensaje de error
            messages.error(request, 'Todos los campos son obligatorios')
            return render(request, 'guardar_mascotas.html')
    
    #Si la peticion no es de tipo POST, entonces renderizamos a guardar_mascotas
    return render(request, 'guardar_mascotas.html')

def editar_mascota(request, id):

    #Tenemos que obtener la mascota que queremos editar
    mascota = get_object_or_404(Mascotas, id=id)  #Obtenermos el id o sino devolvemos un 404

    if request.method == 'POST':

        #Actualizamos la mascota
        mascota.nombre = request.POST.get('nombre')
        mascota.edad = request.POST.get('edad')
        mascota.peso = request.POST.get('peso')
        mascota.especie = request.POST.get('especie')
        mascota.save() #Guardamos los cambios  en la base de datos

        #Mostramos un mensaje de exito
        messages.success(request, 'Mascota actualizada exitosamente')
        return redirect('listar_mascotas_url') #Con redirect Asemos la accion mas ir al otro lado

    else:
        messages.error(request, 'Todos los campos son obligatorios')

    #Si la peticion no es de tipo POST, entonces renderizamos a editar_mascota
    return render(request, 'editar_mascota.html', {'mascota': mascota})

def eliminar_mascota(request, id): #Le pasamos la peticion y el id

    #Tenemos que obtener la mascota que queremos eliminar
    mascota = get_object_or_404(Mascotas, id=id)  #Obtenermos el id o sino devolvemos un 404

    #Eliminamos la mascota
    mascota.delete()

    #Mostramos un mensaje de exito
    messages.success(request, 'Mascota eliminada exitosamente')
    return redirect('listar_mascotas_url') # Con redirect Asemos la accion mas ir al otro lado


def buscar_mascota(request):

    #Obtenemos el nombre de la mascota que queremos buscar
    """
    Busca una mascota en la base de datos por su nombre.
    Si la mascota existe, la renderiza en una plantilla.
    Si no existe, muestra un mensaje de error.
    """

    mascotas = Mascotas.objects.all()

    #Buscamos la mascota en la base de datos
    nombre = request.GET.get('nombre')

    if nombre: #Si la mascota no existe
        mascotas = Mascotas.objects.filter(nombre__contains=nombre).order_by('nombre') #Con el __contains buscamos en el nombre que contenga el nombre buscado (nombre)

    #Renderizamos la lista de mascotas en una plantilla
    #Le pasamos la peticion, el nombre de la plantilla y un diccionario (la lista de mascotas)
    return render(request, 'buscar_mascota.html', {'mascotas': mascotas})