from django.shortcuts import render, get_object_or_404, redirect
from .models import Paises

# Create your views here.
def listar_paises(request):
    paises = Paises.objects.all() #Almacenamos todos los objetos de la tabla en la variable
    return render(request, "listar_paises.html", {'paises': paises})

def guardar_pais(request):
    if request.method == 'POST':
        #Obtenemos los valores desde el los input del formulario
        v_nombre = request.POST.get("nombre")
        v_continente = request.POST.get("continente")
        v_idioma = request.POST.get("idioma")
        v_habitantes = request.POST.get("habitantes")
        v_gobierno = request.POST.get("gobierno")
        
        #Creamos el nuevo objeto
        pais = Paises(
            nombre = v_nombre,
            continente = v_continente,
            idioma = v_idioma,
            habitantes = v_habitantes,
            gobierno = v_gobierno
        )
        
        #Guardamos en la bd
        pais.save()
        
        return redirect('listar_pais_url')
    return render(request, 'guardar_pais.html')

def editar_pais(request, idPais):
    #Buscamos
    pais = get_object_or_404(Paises, pk = idPais)
    
    if request.method == 'POST':
        #Actualizamos los valores
        pais.nombre = request.POST.get('nombre')
        pais.continente = request.POST.get('continente')
        pais.idioma = request.POST.get('idioma')
        pais.habitantes = request.POST.get('habitantes')
        pais.gobierno = request.POST.get('gobierno')
        
        #Guardamos el cambio en la bd
        pais.save()
        
        return redirect('listar_pais_url')
    return render(request, 'editar_pais.html', {'pais': pais})

def eliminar_pais(request, idPais):
    pais = get_object_or_404(Paises, pk=idPais)
    pais.delete() #Eliminamos
    return redirect('listar_pais_url')

def buscar_pais(request):
    query = request.GET.get('nombre', '')
    
    #Expresion ternaria
    paises = Paises.objects.filter(nombre__icontains = query) if query else Paises.objects.all()
    
    # if query:
    #     Paises.objects.filter(nombre__icontains = query)
    # else:
    #     Paises.objects.all()
    return render(request, 'buscar_pais.html', {'paises': paises, 'query': query})