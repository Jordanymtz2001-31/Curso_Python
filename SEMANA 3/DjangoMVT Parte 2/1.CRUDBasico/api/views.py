from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from api.models import Instructores

# Create your views here.
def listar_instructores(request):

    #Pasamos todos los instructores del modelo a unja variable llamada instructores
    instructores = Instructores.objects.all()

    #Redenderizamos la lista de instructores en una plantilla
    #Le pasamos la peticion, el nombre de la plantilla y un diccionario (la lista de instructores)
    return render(request, 'listar_instructores.html', {'instructores': instructores})

def guardar_instructores(request):

    if request.method == 'POST':
        #Obtenemos los datos del formulario de la plantillas
        name = request.POST.get('name')
        age = request.POST.get('age')
        curso = request.POST.get('curso')
        experiens = request.POST.get('experiens')

        #Validamos los datos que no esten vacios
        if name and age and curso and experiens:
            #Creamos un nuevo instructor
            Instructores.objects.create(
                name=name,
                age=int(age),
                curso=curso,
                experiens=experiens
            )

            #Mostramos un mensaje de exito
            messages.success(request, 'Instructor creado exitosamente')
            #Redirigimos al usuario a la lista de instructores
            return redirect('listar_instructores_url') #Con redirect Asemos la accion mas ir al otro lado

        else:
            #Mostramos un mensaje de error
            messages.error(request, 'Todos los campos son obligatorios')
            return render(request, 'guardar_instructores.html')
        
    #Si la peticion no es de tipo POST, entonces renderizamos a guardar_instructores
    return render(request, 'guardar_instructores.html' ) #Con render le pasamos la peticion y la plantilla

def editar_instructor(request, id):
    #Tenemos que obtener el instructor que queremos editar
    instructor = get_object_or_404(Instructores, id=id)  #Obtenermos el id o sino devolvemos un 404

    if request.method == 'POST':

        #Actualizamos el instructor
        instructor.name = request.POST.get('name')
        instructor.age = request.POST.get('age')
        instructor.curso = request.POST.get('curso')
        instructor.experiencia = request.POST.get('experiencia')
        instructor.save() #Guardamos los cambios  en la base de datos

        #Mostramos un mensaje de exito
        messages.success(request, 'Instructor actualizado exitosamente')
        return redirect('listar_instructores_url')

    else:
        messages.error(request, 'Todos los campos son obligatorios')

    #Si la peticion no es de tipo POST, entonces renderizamos a editar_instructor
    return render(request, 'editar_instructor.html', {'instructor': instructor})

def eliminar_instructor(request, id): #Le pasamos la peticion y el id

    #Tenemos que obtener el instructor que queremos eliminar
    instructor = get_object_or_404(Instructores, id=id)  #Obtenermos el id o sino devolvemos un 404

    #Eliminamos el instructor
    instructor.delete()

    #Mostramos un mensaje de exito
    messages.success(request, 'Instructor eliminado exitosamente')
    return redirect('listar_instructores_url') # Con redirect Asemos la accion mas ir al otro lado

def buscar_instructor(request):
    #Obtenemos el valor del curso desde el formulario con clave "curso_busqueda" y sino tiene valor tomara un string vacio

    """
    Esta funcion busca instructores que coincidan con el curso buscado desde un formulario.
    Si el curso buscado es vacio, devuelve todos los instructores.
    La funcion devuelve una renderizacion de la plantilla 'buscar_instructor.html' con la lista de instructores y el curso buscado.
    """
    curso_buscado = request.GET.get('curso_busqueda', '')# Con get obtenemos el valor de la clave ya sea que este vacio o no

    if curso_buscado:
        #Buscamos los instructores que coincidan con el curso
        instructores = Instructores.objects.filter(curso__icontains=curso_buscado) #Con el __icontains buscamos en el curso que contenga el curso buscado (curso_buscado)
    else:
        #Mostramos todos los instructores
        instructores = Instructores.objects.all()

    #Renderizamos la lista de instructores y el curso en una plantilla
    return render(request, 'buscar_instructor.html', {'instructores': instructores}, {'curso_buscado': curso_buscado})
