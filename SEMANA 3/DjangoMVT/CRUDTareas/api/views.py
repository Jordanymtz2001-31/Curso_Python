from django.shortcuts import render, redirect
from .forms import TareaForm
from .models import Tarea

# Create your views here.
def listar_y_crear(request):
    if request.method == 'POST': #Si es un POST, se GUARDA
        #Inicializamos el formulario con los datos de la peticion
        form = TareaForm(request.POST)
        #Validamos el formulario
        if form.is_valid():
            #Guardamos
            form.save()
            return redirect('listar_tareas_url')
    else:
        # Si no es un POST entonces creamos un formulario vacio
        form = TareaForm()
        
    #Obtenemos tareas completas e incompletas
    tareas_completadas = Tarea.objects.filter(completado = True)
    tareas_incompletas = Tarea.objects.filter(completado = False)
    
    return render(request, 'tareas_listar.html', {
        'formulario': form,
        'completadas': tareas_completadas,
        'incompletas': tareas_incompletas
    })
    
def update_tareas(request, tarea_id):
    if request.method == 'POST':
        #Buscamos la tarea
        tarea = Tarea.objects.get(id = tarea_id)
        #Modificamos el valor del campo "completado"
        tarea.completado = not tarea.completado #El valor sera igual al valor contrario
        tarea.save()
    return redirect('listar_tareas_url')
