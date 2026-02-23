from django.shortcuts import render
from api.forms import TareaForm
from api.models import Tarea
from django.shortcuts import redirect

#En esta funcion lo que hace es que podemos ver la lista de tareas ya sea completadas o incompletadas 
# Y al mismo tiempo podemos crear una nueva tarea
def listar_y_crear(request):
    if request.method == 'POST':
        formulario = TareaForm(request.POST) #Inicializamos el formulario con los datos del POST
        if formulario.is_valid(): #Con is_valid valida todos los datos de los campos del formulario
            formulario.save() #Guardamos los datos en la base de datos
            return redirect('listar_tareas_url') #Redirigimos al usuario a la lista de tareas

    else:
        formulario = TareaForm() #Inicializamos el formulario

    tareas_completadas = Tarea.objects.filter(completed = True) #Obtenemos todas las tareas que esten completadas
    tareas_incompletadas = Tarea.objects.filter(completed = False) #Obtenemos todas las tareas que no esten completadas

    #Renderizamos la lista de tareas ya sea completadas o incompletadas en una plantilla
    return render(request, 'listar_y_crear.html', {'formulario': formulario, 
                                                    'completadas': tareas_completadas, 
                                                    'incompletadas': tareas_incompletadas})

def editar_tarea(request, id):
    if request.method == 'POST':
        tarea = Tarea.objects.get(id=id) #Obtenemos la tarea que queremos editar
        tarea.completed = not tarea.completed #Cambiamos el estado de la tarea
        tarea.save() #Guardamos los cambios en la base de datos
        return redirect('listar_tareas_url') #Redirigimos al usuario a la lista de tareas