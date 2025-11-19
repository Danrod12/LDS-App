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
    # ordenanza = [
    #     ("BAUSTISMO","Bautismo"),
    #     ("VICARIO","Bautismo Vicario"),
    #     ("Activacion","Activación"),
    #     ("INVESTIDURA","Investidura"),
    #     ("SELLAMIENTO","Sellamiento")
    # ]

    organizacion = models.CharField(max_length=100, choices=organizaciones, verbose_name='Organizacion', blank=True, null=True)
    condicion_actual = models.CharField(max_length=100, choices=condicion, verbose_name='Condición Actual', blank=True, null=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre', blank=True, null=True)
    meta = models.TextField(verbose_name='Meta', blank=True, null=True)
    ordenanza_faltante = models.CharField(max_length=100, choices=ordenanza, verbose_name='Ordenanza Faltante', blank=True, null=True)
    fecha_establecida = models.DateField(verbose_name='Fecha Establecida', blank=True, null=True)
    fecha_meta = models.DateField(verbose_name='Fecha de Meta', blank=True, null=True)
    done = models.BooleanField(default=False, verbose_name='Completado')
    # ordenanza_faltante = models.CharField(max_length=100, choices=ordenanza, verbose_name='Ordenanza Faltante', blank=True, null=True)

    # ✔️ Arreglo: campo funcionando correctamente:

    def __str__(self):
        return self.nombre if self.nombre else "(Sin nombre)"

class SocSoc:
    # @staticmethod
    # def importar_desde_csv(ruta_archivo):
    #     with open(ruta_archivo, newline='', encoding='utf-8') as csvfile:
    #         lector = csv.DictReader(csvfile)
    #         for fila in lector:
    #             ObraMisional.objects.create(
    #                 organizacion=fila['organizacion'],
    #                 condicion_actual=fila['condicion_actual'],
    #                 nombre=fila['nombre'],
    #                 meta=fila['meta'],
    #                 ordenanza_faltante=fila['ordenanza_faltante'],
    #                 fecha_establecida=fila['fecha_establecida'],
    #                 fecha_meta=fila['fecha_meta'],
    #                 done=(fila['done'].strip().lower() == 'true')
    #             )
    pass

class Quorum:
    pass    
class MujeresJovenes:
    pass    
class HombresJovenes:
    pass
class Primaria:
    pass
