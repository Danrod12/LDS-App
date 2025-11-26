from django import forms
from .models import *

class ObraMisionalForm(forms.ModelForm):

    class Meta:
        model = ObraMisional
        fields = [
            'organizacion',
            'condicion_actual',
            'nombre',
            'meta',
            'ordenanza_faltante',
            'fecha_meta'
        ]
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
                'placeholder': 'Ej: Visita a la familia Pérez',
                'id': 'id_nombre'
            }),
            'meta': forms.Select(attrs={
                'class': 'form-select',
                'id': 'id_meta'
            }),
            'ordenanza_faltante': forms.Select(attrs={
                'class': 'form-select',
                'id': 'id_ordenanza_faltante'
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
            'fecha_meta': 'Fecha meta',
        }

    # ----------------------------------------------
    #  METAS DINÁMICAS SEGÚN LA CONDICIÓN ACTUAL
    # ----------------------------------------------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        condicion = None

        # Para POST (cuando el usuario cambia condicion_actual)
        if "condicion_actual" in self.data:
            condicion = self.data.get("condicion_actual")

        # Para EDICIÓN (si el objeto ya existe)
        elif self.instance.pk:
            condicion = self.instance.condicion_actual

        # Asignar lista correcta
        if condicion == "MENOS_ACTIVOS":
            self.fields["meta"].choices = Meta.MENOS_ACTIVOS
        
        elif condicion == "ACTIVOS":
            self.fields["meta"].choices = Meta.ACTIVOS

        elif condicion == "CONVERSOS":
            self.fields["meta"].choices = Meta.CONVERSOS

        elif condicion in ["QUORUM", "SOCSOC"]:
            self.fields["meta"].choices = Meta.QUORUM_SOCSOC

        elif condicion in ["HOMBRES", "MUJERES"]:
            self.fields["meta"].choices = Meta.JOVENES

        elif condicion == "INVESTIGADORES":
            self.fields["meta"].choices = Meta.INVESTIGADORES
