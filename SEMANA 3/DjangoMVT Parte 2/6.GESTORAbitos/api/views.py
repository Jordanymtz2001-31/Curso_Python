from django.shortcuts import render
from api.forms import HabitatsForm
from api.models import Habitats
from django.shortcuts import redirect

# En esta funcion lo que hace es que podemos ver la lista de habitos ya sea completadas o incompletadas 
# Y al mismo tiempo podemos crear una nueva tarea
def listar_y_crear(request):
    if request.method == 'POST':
        formulario = HabitatsForm(request.POST) #Inicializamos el formulario con los datos del POST
        if formulario.is_valid(): #Con is_valid valida todos los datos de los campos del formulario
            formulario.save() #Guardamos los datos en la base de datos
            return redirect('listar_habitos_url') #Redirigimos al usuario a la lista de tareas

    else:
        formulario = HabitatsForm() #Inicializamos el formulario

    habitos_completadas = Habitats.objects.filter(completed = True) #Obtenemos todas las tareas que esten completadas
    habitos_incompletadas = Habitats.objects.filter(completed = False) #Obtenemos todas las tareas que no esten completadas

    #Renderizamos la lista de tareas ya sea completadas o incompletadas en una plantilla
    return render(request, 'listar_y_crear.html', {'formulario': formulario,
                                                    'completadas': habitos_completadas,
                                                    'incompletadas': habitos_incompletadas})

#Metodo para editar el estados de los habitos
def editar_estado_habito(request, id):
    if request.method == 'POST':
        habito = Habitats.objects.get(id=id)
        habito.completed = not habito.completed #Por default es False pero cuando se da click se cambia al True, sucede con el checkbox en la plantilla
        habito.save()
        return redirect('listar_habitos_url')

#Metodo para editar un habito
def editar_habito(request, id):
    habito = Habitats.objects.get(id=id)

    if request.method == 'POST':
        formulario = HabitatsForm(request.POST, instance=habito)  # instance= carga datos existentes
        if formulario.is_valid(): #Con is_valid valida todos los datos de los campos del formulario
            formulario.save()  # Actualiza hábito existente
            return redirect('listar_habitos_url')
    else:
        formulario = HabitatsForm(instance=habito)  # Carga datos para editar
    return render(request, 'editar_habito.html', {'formulario': formulario})

#Metodo para eliminar un habito
def eliminar_habito(request, id):
    habito = Habitats.objects.get(id=id)
    habito.delete()
    return redirect('listar_habitos_url')