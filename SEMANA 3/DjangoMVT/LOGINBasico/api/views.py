from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
#Creamos credenciales en memoria
USUARIO_MEMORIA = {
    'username' : 'miranda',
    'password': '1234',
    'nombre': 'Miranda'
}

def login_view(request):
    if request.method == 'POST':
        #Obtenemos los valores desde el formulario
        username = request.POST['username']
        password = request.POST['password']
        
        #Imprimimos las credenciales en consola (util para depuracion)
        print("Usuario: ", username)
        print("Contraseña: ", password)
        
        #Verificamos que las credenciales en memoria sean correctas
        if username == USUARIO_MEMORIA['username'] and password == USUARIO_MEMORIA['password']:
            # Guardamos el nombre del usuario en la session actual
            request.session['usuario_autenticado'] = USUARIO_MEMORIA['nombre']
            #Redirigimos al dashboard
            return redirect('dashboard')
        else:
            messages.error(request, 'Credenciales incorrectas.')
            
    return render(request, 'login.html')
            
            
def dashboard_view(request):
    #Recuperamos el nombre del usuario autenticado
    nombre = request.session.get('usuario_autenticado', None)
    # Si no existe nombre significa que el usuario no se autentico
    if not nombre:
        #Lo redirigimos al login
        return redirect('login')
    #Si si se autentico, entonces lo renderizamos al dashboard
    return render(request, 'dashboard.html', {'nombre': nombre})

def logout_view(request):
    #Borramos toda la informacion de la session
    request.session.flush()
    #Una vez que cerramos la sesion, regresamos al login
    return redirect('login')
