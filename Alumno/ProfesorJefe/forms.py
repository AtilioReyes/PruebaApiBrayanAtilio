from django import forms

from .models import *

class FormProfeJefe(forms.ModelForm):
    class Meta: 
        model = ProfJefe
        fields = '__all__'