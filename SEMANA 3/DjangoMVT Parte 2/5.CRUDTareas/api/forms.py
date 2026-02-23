# Creamos el formulario a base de nuestp modelo
from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea #Definimos el modelo que queremos usar
        fields = ['title', 'description'] #Definimos los campos que queremos usar

        #Agregamos un estilo a los campos que se van a mostrar en el formulario
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título de la tarea'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ingrese la descripción de la tarea'}),
        }