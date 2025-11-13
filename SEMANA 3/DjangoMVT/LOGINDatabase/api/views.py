from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        #Obtenemos los valores de las credenciales desde el login
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username= username, password = password)
        print("User: ", user) #Depuracion
        
        if user is not None: #Su el usuario existe
            login(request, user) #Iniciamos sesion
            return redirect('dashboard')
        else:
            messages.error(request, 'Credenciales incorrectas.')
            
    return render(request, 'login.html')

def registro_view(request):
    if request.method == 'POST':
        #Inicializamos el formulario con todos los valores de los input
        form = RegistroForm(request.POST)
        if form.is_valid(): #Validamos si los datos son correctos
            form.save() #Guardamos en la bd
            messages.success(request, 'Usuario registrado correctamente!')
            return redirect('login')
        else:
            messages.warning(request, 'Por favor corrige los errores.')
    else: #Si no es POST
        #Se incializa el formulario vacio
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

#Vista protegida
@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'usuario': request.user})

def logout_view(request):
    logout(request) #Eliminamos la sesion del usuario
    return redirect('login')
