from decimal import Decimal
from django.shortcuts import get_object_or_404, render
from api.models import Alumno
from django.contrib import messages
from django.shortcuts import redirect

# Creacion de modelos 
# views.py
def listar_alumnos(request):
    # 1. TODOS los alumnos
    todos_alumnos = Alumno.objects.all()
    
    # 2. Solo aprobados
    alumnos_aprobados = Alumno.objects.filter(estatus='Aprobado')
    
    # 3. Solo reprobados
    alumnos_reprobados = Alumno.objects.filter(estatus='Reprobado')
    
    return render(request, 'listar_alumnos.html', {
        'todos_alumnos': todos_alumnos,
        'alumnos_aprobados': alumnos_aprobados,
        'alumnos_reprobados': alumnos_reprobados
    })

def guardar_alumno(request):
    
    if request.method == 'POST':

        nombreE = request.POST.get('nombre')
        edadE = int(request.POST.get('edad'))
        apellidoE = request.POST.get('apellido')
        gradoE = request.POST.get('grado')
        calificacionE =Decimal(request.POST.get('calificacion'))

        Alumno.objects.create(
            nombre=nombreE,
            apellido=apellidoE,
            edad=edadE,
            grado=gradoE,
            calificacion=calificacionE
        )

        messages.success(request, 'Empleado creado exitosamente')
        return redirect('listar_alumnos_url')
    
    return render(request, 'guardar_alumno.html')

def editar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)

    if request.method == 'POST':
        #Aqui ya tenemos los datos del formulario y entonces podemos actualizar el empleado
        alumno.nombre = request.POST.get('nombre')
        alumno.apellido = request.POST.get('apellido')
        alumno.edad = request.POST.get('edad')
        alumno.grado = request.POST.get('grado')
        alumno.calificacion = Decimal(request.POST.get('calificacion'))
        alumno.save()

        

        messages.success(request, 'Empleado actualizado exitosamente')
        return redirect('listar_alumnos_url')

    return render(request, 'editar_alumno.html', {'alumno': alumno})

def eliminar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    alumno.delete()

    messages.success(request, 'Empleado eliminado exitosamente')
    return redirect('listar_alumnos_url')

def buscar_alumnos_por_grado(request):
    grado = request.GET.get('grado', '') #Indicamos que nos regrese un string vacio en caso de que no haya ningun parametro

    alumnos = Alumno.objects.filter(grado__icontains=grado) if grado else Alumno.objects.all() #Indicamos que si grado es vacio entonces liste todos

    return render(request, 'buscar_alumnos.html', {'alumnos': alumnos, 'grado': grado})