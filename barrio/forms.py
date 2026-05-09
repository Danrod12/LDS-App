from django import forms
from .models import *

class PersonaForm(forms.ModelForm):

    # FORM DE PERSONA
    class Meta:
        model = Persona

        fields = [
            'organizacion',
            'condicion_actual',
            'nombre',
            'ordenanza_faltante',
        ]
        widgets = {
            #  'persona': forms.Select(attrs={
            #     'class': 'form-select',
            #     'id': 'id_persona'
            # }),
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
            
            'ordenanza_faltante': forms.Select(attrs={
                'class': 'form-select',
                'id': 'id_ordenanza_faltante'
            }),
            
        }
        labels = {
            'organizacion': 'Organización',
            'condicion_actual': 'Condición Actual',
            'nombre': 'Nombre',
            'ordenanza_faltante': 'Ordenanza Faltante',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        condicion = None

            # Para POST (cuando el usuario cambia condicion_actual)
        if "condicion_actual" in self.data:
            condicion = self.data.get("condicion_actual")
        #  METAS DINÁMICAS SEGÚN LA CONDICIÓN ACTUAL
        # ----------------------------------------------

            # Para EDICIÓN (si el objeto ya existe)
        elif self.instance.pk:
            condicion = self.instance.condicion_actual

class ObraMisionalForm(forms.ModelForm):

    class Meta:
        model = ObraMisional

        fields = [
            'persona',
            'meta',
            'fecha_meta',
            'responsable',
            'nota',
        ]

        widgets = {

            'persona': forms.Select(attrs={
                'class': 'form-select',
                'id': 'id_persona'
            }),

            'meta': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_meta'
            }),

            'fecha_meta': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'id': 'id_fecha_meta'
            }),

            'responsable': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_responsable'
            }),
            'nota': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_nota',
            }),

        }

        labels = {

            'persona': 'Persona',
            'meta': 'Meta',
            'fecha_meta': 'Fecha Meta',
            'responsable': 'Responsable',
            'nota': 'Nota',

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        condicion = None

        # Cuando el usuario selecciona persona
        if "persona" in self.data:

            try:
                persona_id = self.data.get("persona")
                persona = Persona.objects.get(id=persona_id)

                condicion = persona.condicion_actual

            except:
                pass

        # Cuando se está editando
        elif self.instance.pk and self.instance.persona:

            condicion = self.instance.persona.condicion_actual

    # ----------------------------------------------

        # Asignar lista correcta
        # if condicion == "MENOS_ACTIVOS":
        #     self.fields["meta"].choices = Meta.MENOS_ACTIVOS
        
        # elif condicion == "ACTIVOS":
        #     self.fields["meta"].choices = Meta.ACTIVOS

        # elif condicion == "CONVERSOS":
        #     self.fields["meta"].choices = Meta.CONVERSOS

        # elif condicion in ["QUORUM", "SOCSOC"]:
        #     self.fields["meta"].choices = Meta.QUORUM_SOCSOC

        # elif condicion in ["HOMBRES", "MUJERES"]:
        #     self.fields["meta"].choices = Meta.JOVENES

        # elif condicion == "INVESTIGADORES":
        #     self.fields["meta"].choices = Meta.INVESTIGADORES
