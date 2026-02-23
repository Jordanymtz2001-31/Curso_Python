#Creamos nuestro formulario
from django import forms
from .models import Habitats

class HabitatsForm(forms.ModelForm):
    class Meta:
        model = Habitats #Definimos el modelo que queremos usar
        fields = ['title', 'description'] #Definimos los campos que queremos usar y que se podran editar

        #Definimos los widgets para los campos junto con sus estilos
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título del habito'}), #Definimos el estilo del campo
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ingrese la descripción del habito'}), #Definimos el estilo del campo
        }