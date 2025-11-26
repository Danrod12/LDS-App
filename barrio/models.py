from django.db import models
import csv

class ObraMisional(models.Model):
    organizaciones = [
        ("QUORUM", "Quorum de Elderes"),
        ("SOCSOC", "Sociedad de Socorro"),
        ("MUJERES", "Mujeres Jóvenes"),
        ("HOMBRES", "Hombres Jóvenes"),
        ("PRIMARIA", "Primaria")
    ]

    condicion = [
        ("INVESTIGADOR","Investigador"),
        ("CONVERSO","Converso"),
        ("LESSACTIVE","Menos Activo"),
        ("ACTIVO","Activo")
    ]

    ordenanza = [
        ("BAUSTISMO","Bautismo"),
        ("VICARIO","Bautismo Vicario"),
        ("Activacion","Activación"),
        ("INVESTIDURA","Investidura"),
        ("SELLAMIENTO","Sellamiento")
    ]
    
    goal = [("LEER","Leer las Escrituras"),
            ("ORAR ","Orar"),]


    organizacion = models.CharField(max_length=100, choices=organizaciones, verbose_name='Organizacion', blank=True, null=True)
    condicion_actual = models.CharField(max_length=100, choices=condicion, verbose_name='Condición Actual', blank=True, null=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre', blank=True, null=True)
    meta = models.TextField(verbose_name='Meta', blank=True, null=True)
    ordenanza_faltante = models.CharField(max_length=100, choices=ordenanza, verbose_name='Ordenanza Faltante', blank=True, null=True)
    fecha_establecida = models.DateField(verbose_name='Fecha Establecida', blank=True, null=True)
    fecha_meta = models.DateField(verbose_name='Fecha de Meta', blank=True, null=True)
    done = models.BooleanField(default=False, verbose_name='Completado')

    def __str__(self):
        return self.nombre if self.nombre else "(Sin nombre)"

# class LoginUser(models.Model):
    
#     organizaciones = [
#         ("QUORUM", "Quorum de Elderes"),
#         ("SOCSOC", "Sociedad de Socorro"),
#         ("MUJERES", "Mujeres Jóvenes"),
#         ("HOMBRES", "Hombres Jóvenes"),
#         ("PRIMARIA", "Primaria"),
#         ("OBISPADO", "Obispado"),
#     ]

#     pin = models.CharField(max_length=10, unique=True, verbose_name="PIN")
#     organizacion = models.CharField(max_length=20, choices=organizaciones)

#     def __str__(self):
#         return f"{self.organizacion} ({self.pin})"
