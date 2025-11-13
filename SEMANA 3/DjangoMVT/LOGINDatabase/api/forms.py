from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Esta clase hereda de UserCrearionForm que es un formulario que incluye todos los campos
# del sistema de usuarios de django y la usaremos para personalizar el formulario de registro.
class RegistroForm(UserCreationForm):
    last_name = forms.CharField(
        label = 'Nombre', #Texto que se muestra junto al input en el formulario
        max_length=50, #Maximos 50 caracteres
        widget= forms.TextInput(attrs={ #Definimos los elementos html del input
            'class': 'form-control',
            'placeholder': 'Ingresa tu nombre'
        })
    )
    
    email = forms.EmailField(
        label = 'Correo',
        widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu correo'
        })
    )
    
    username = forms.CharField(
        label = 'Usuario',
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu usuario'
        })
    )
    
    password1 = forms.CharField(
        label = 'Contraseña',
        widget= forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa la contraseña'
        })
    )
    
    password2 = forms.CharField(
        label = 'Confirmar contraseña',
        widget= forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirma tu contraseña'
        })
    )
    
    class Meta:
        model = User
        fields = ['last_name', 'username', 'email', 'password1', 'password2']
    