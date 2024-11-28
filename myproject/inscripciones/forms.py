from django import forms
from .models import TertuliaForm


class TertuliaRegistro(forms.ModelForm):
    class Meta:
        model = TertuliaForm
        fields = ['nombre', 'apellido', 'edad', 'email', 'numero_telefono', 'nombre_tertulia', 'tertulia_folio_id']
