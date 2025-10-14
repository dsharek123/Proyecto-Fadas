from django import forms
from .models import Apunte

class ApunteForm(forms.ModelForm):
    class Meta:
        model = Apunte
        fields = ['titulo', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Titulo del apunte'}),
            'contenido': forms.Textarea(attrs={'placeholder':'Escribe tus apuntes aqui...'})
        }