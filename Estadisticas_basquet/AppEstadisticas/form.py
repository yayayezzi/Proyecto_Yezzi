from django import forms
from .models import Equipo, Jugador, Liga

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'

class LigaForm(forms.ModelForm):
    class Meta:
        model = Liga
        fields = '__all__'
