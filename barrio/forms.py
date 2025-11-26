from django import forms
from .models import ObraMisional

class ObraMisionalForm(forms.ModelForm):
    class Meta:
        model = ObraMisional
        fields = ['organizacion', 'condicion_actual', 'nombre', 'meta','ordenanza_faltante','fecha_establecida', 'fecha_meta']
        widgets = {
            'organizacion': forms.Select(attrs={
                'class': 'form-select',
                'id': 'id_organizacion'
            }),
            'condicion_actual': forms.Select(attrs={
                'class': 'form-select',
                'id': 'id_condicion_actual'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Bautismo de la familia Pérez',
                'id': 'id_nombre'
            }),
            'meta': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Bautismo de la familia Pérez',
                'id': 'id_meta'
            }),
            'ordenanza_faltante': forms.Select(attrs={
                'class': 'form-select',
                'id': 'id_ordenanza_faltante'
            }),
            'fecha_establecida': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'id': 'id_fecha_establecida'
            }),
            'fecha_meta': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'id': 'id_fecha_meta'
            }),
        }
        labels = {
            'organizacion': 'Organización',
            'condicion_actual': 'Condición Actual',
            'nombre': 'Nombre',
            'meta': 'Meta',
            'ordenanza_faltante': 'Ordenanza Faltante',
            'fecha_establecida': 'Establecido',
            'fecha_meta': 'Fecha meta',
        }

# class LoginForm(forms.Form):
#     pin = forms.CharField(label="PIN", widget=forms.PasswordInput)
