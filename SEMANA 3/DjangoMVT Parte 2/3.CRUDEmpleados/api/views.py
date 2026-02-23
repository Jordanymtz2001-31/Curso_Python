from django.shortcuts import get_object_or_404, render
from api.models import Empleados
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def listar_empleados(request):
    empleados = Empleados.objects.all()

    return render(request, 'listar_empleados.html', {'empleados': empleados})

def guardar_empleados(request):
    """
    Guarda un empleado en la base de datos.
    Si la peticion es de tipo POST, obtenemos los datos del formulario y los guardamos en la base de datos.
    Si no es de tipo POST, renderizamos la plantilla 'guardar_empleado.html'
    """
    if request.method == 'POST':
        
        nombreE = request.POST.get('nombre')
        puestoE = request.POST.get('puesto')
        sueldoE = float(request.POST.get('sueldo') or 0)
        departamentoE = request.POST.get('departamento')

        Empleados.objects.create(
            nombre=nombreE,
            puesto=puestoE,
            sueldo=sueldoE,
            depa=departamentoE
        )

        messages.success(request, 'Empleado creado exitosamente')
        return redirect('listar_empleados_url')
    
    return render(request, 'guardar_empleado.html')

def editar_empleado(request, id):
    """
    Al momento de pasar el id del empleado a editar, obtenemos el empleado de la base de datos y estos los podemos cargar en la plantilla
    Si la peticion es de tipo POST, obtenemos los datos del formulario y los guardamos en la base de datos.
    Si no es de tipo POST, renderizamos la plantilla 'editar_empleado.html' con el empleado a editar.
    """
    empleado = get_object_or_404(Empleados, id=id)

    if request.method == 'POST':
        #Aqui ya tenemos los datos del formulario y entonces podemos actualizar el empleado
        empleado.nombre = request.POST.get('nombre')
        empleado.puesto = request.POST.get('puesto')
        empleado.sueldo = float(request.POST.get('sueldo') or 0)
        empleado.depa = request.POST.get('departamento')
        empleado.save()

        messages.success(request, 'Empleado actualizado exitosamente')
        return redirect('listar_empleados_url')

    return render(request, 'editar_empleado.html', {'empleado': empleado})

def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleados, id=id)
    empleado.delete()

    messages.success(request, 'Empleado eliminado exitosamente')
    return redirect('listar_empleados_url')

def buscar_empleado(request):

    """
    Busca empleados en la base de datos por su nombre.
    Si se pasa un parametro de busqueda por GET, se busca en la base de datos con el nombre que se pasa.
    Si no se pasa parametro de busqueda por GET, se devuelve la lista completa de empleados.
    La funcion devuelve una renderizacion de la plantilla 'listar_empleados.html' con la lista de empleados.
    """
    busqueda_nombre = request.GET.get('busqueda', '') #Indicamos que nos regrese un string vacio en caso de que no haya ningun parametro

    empleados = Empleados.objects.filter(nombre__icontains=busqueda_nombre) if busqueda_nombre else Empleados.objects.all() #Indicamos que si busqueda_nombre es vacio entonces liste todos

    #Renderizamos la plantilla y carga la lista de empleados en caso de que busqueda_nombre no sea vacio 
    #O el empleado que coincidan con el nombre que se metio en el formulario
    return render(request, 'buscar_empleado.html', {
        'empleados': empleados,  
        'busqueda_nombre': busqueda_nombre
        })
