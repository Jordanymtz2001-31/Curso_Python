from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):

    first_name = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ingrese su nombre"
            }),
        required=True
    )

    email= forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Ingrese su email"
            }),
        required=True
    )

    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ingrese su usuario"
            }),
        required=True
    )

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Ingrese su contraseña"
            }),
        required=True
    )

    password2 = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirme su contraseña"
            }),
        required=True
    )

    class Meta:
        model = User #Definimos el modelo
        fields = ['first_name', 'email', 'username', 'password1', 'password2'] #Definimos los campos que se mostraran en el formulario