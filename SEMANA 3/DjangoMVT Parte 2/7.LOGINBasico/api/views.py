from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

#Credencias en memoria
CREDENCIALES = {
    'username': 'dany',
    'password': '1234',
    'nombre': 'Dany',
}

def login_view(request):
    if request.method == 'POST':
        #Obtenemos los datos del formulario que ingresa el usuario
        username = request.POST.get('username')
        password = request.POST.get('password')

        #Validamos las credenciasles que el usuariuo ingrese en el formulario de login
        if username == CREDENCIALES['username'] and password == CREDENCIALES['password']:

            #Si las credenciales son correctas, guardamos el username en la sesion
            request.session['username_autenticado'] = CREDENCIALES['username']

            # Y redireccionamos al dashboard (es decir a la pagina principal)
            return redirect('dashboard_url')
        else: # Si las credenciales son incorrectas entonces mostramos un error en la plantilla de login
            messages.error(request, 'Credenciales incorrectas')
    # Si la peticion no es de tipo POST, entonces renderizamos a login
    return render(request, 'login.html')
    
def dashboard_view(request):
    #Obtenbemos el usuario que esta autenticado en el login
    user = request.session.get('username_autenticado')

    #Validamos si el usuario esta autenticado
    if user:
        #Si el usuario esta autenticado, mostramos el dashboard
        return render(request, 'dashboard.html', {'user': user})
    #Si el usuario no esta autenticado, redireccionamos al login
    return redirect('login_url')

#Vista para cuanso uno sale de la sesion
def logout_view(request):
    #Limpiamos la sesion
    request.session.flush()

    #Redireccionamos al login
    return redirect('login_url')