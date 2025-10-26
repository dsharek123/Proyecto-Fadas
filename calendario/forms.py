from django import forms
from .models import Tema

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['tema', 'actividad', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }