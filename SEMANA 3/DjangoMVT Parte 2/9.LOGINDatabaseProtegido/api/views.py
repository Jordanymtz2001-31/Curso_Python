
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from api.forms import RegistroForm, ProductosForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from api.models import Producto

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        #Obtenemos los datos del formulario que el usuario ingreso en la plantilla
        username = request.POST.get('username')
        password = request.POST.get('password')

        #Autenticamos al usuario con los datos que el usuario ingreso
        user = authenticate(request, username=username, password=password)

        
        if user is not None: #Si el usuario existe
            login(request, user)
            messages.success(request, 'Login exitoso') #Mandamos mensaje de exito
            return redirect('dashboard')
            
        
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    #Si la peticion no es de tipo POST, entonces renderizamos a login
    return render(request, 'login.html')


def registro_view(request):
    if request.method == "POST":
        #Obtenemos los datos del formulario 
        formulario = RegistroForm(request.POST)
        if formulario.is_valid(): #Si el formulario es valido
            formulario.save() #Guardamos los datos en la base de datos
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('login')
        else:
            messages.warning(request, 'Error al crear el usuario')
    else:
        formulario = RegistroForm() #Inicializamos el formulario
    #Le pasamos la peticion, el nombre de la plantilla y un diccionario (el formulario)
    return render(request, 'registro.html', {'formulario': formulario})

#Vista protegida
@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def listar_view(request):
    #Obtenemos todos los productos y las pasamos a la variable
    productos = Producto.objects.all()

    #Le pasamos la peticion, el nombre de la plantilla y un diccionario (la lista de productos)
    return render(request, 'listar.html', {'productos': productos})

@login_required
def guardar_view(request):
    if request.method == 'POST':
        formulario = ProductosForm(request.POST) #Inicializamos el formulario con los datos del POST
        if formulario.is_valid(): #Con is_valid valida todos los datos de los campos del formulario
            formulario.save() #Guardamos los datos en la base de datos
            return redirect('listar') #Redirigimos al usuario a la lista de productos
    else:
        formulario = ProductosForm()
    return render(request, 'guardar.html', {'formulario': formulario})

@login_required
def editar_view(request, id):
    producto = Producto.objects.get(id=id)

    if request.method == 'POST':
        formulario = ProductosForm(request.POST, instance=producto)  # instance= carga datos existentes
        if formulario.is_valid(): #Con is_valid valida todos los datos de los campos del formulario
            formulario.save()  # Actualiza producto existente
            return redirect('listar')
    else:
        formulario = ProductosForm(instance=producto)  # Carga datos para editar
    return render(request, 'editar.html', {'formulario': formulario})

@login_required
def eliminar_view(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('listar')