from django import forms

from . import models


class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ["nombre", "apellido", "nacimiento", "pais_origen"]


class ClienteBuscarFormulario(forms.Form):
    nombre = forms.CharField
    apellido = forms.CharField
    nacimiento = forms.DateField
    pais_origen = forms.CharField