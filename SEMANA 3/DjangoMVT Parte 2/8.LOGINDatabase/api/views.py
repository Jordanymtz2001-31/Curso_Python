from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from api.forms import RegistroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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