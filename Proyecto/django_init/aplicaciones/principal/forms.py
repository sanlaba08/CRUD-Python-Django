from django import forms
from .models import Persona

class personaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

