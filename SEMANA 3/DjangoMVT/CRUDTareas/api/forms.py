from django import forms 
from .models import Tarea

""" 
El archivo forms.py sirve para definir formularios personalizados que manejen
la entrada de datos del usuario.
"""

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea #Definimos el modelo que se usara
        #Especifico los campos que quiero usar
        fields = ['titulo', 'descripcion']
        #Especificamos los elementos HTML que vamos a usar.
        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el titulo de la tarea.'}),
            
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ingresa la descripcion'})
        }
        
        """ 
        <input type = "text" placeholder = "Ingresa el titulo de la tarea." class = "form-control">
        
        <textarea placeholder=  "Ingresa la descripcion" rows = "3" class = "form-control"> 
        """