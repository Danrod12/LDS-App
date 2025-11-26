from django.db import models


# ============================================
#   LISTAS DE METAS SEGÚN CONDICIÓN
# ============================================
class Meta(models.Model):

    MENOS_ACTIVOS = [
        ("MA_DOMINGOS4", "Llegar 4 domingos consecutivos"),
        ("MA_ACTIVIDADES", "Ir a actividades de la iglesia"),
        ("MA_HOGAR", "Hacer noches de hogar"),
        ("MA_TEMPLO", "Ir al templo"),
        ("MA_EDUCACION", "Participar en programas de educación BYU / Becas / FPE / Mentors"),
        ("MA_ARBOL", "Trabajar en su árbol familiar"),
    ]

    ACTIVOS = [
        ("AC_AMIGOS", "Hacerse de uno o más amigos recién conversos"),
        ("AC_TEMPLO", "Ir al templo"),
        ("AC_MISIONEROS", "Apoyar en las visitas con los misioneros"),
        ("AC_EDUCACION", "Participar en programas de educación BYU / Becas / FPE / Mentors"),
        ("AC_ACTIVIDADES", "Participar de las actividades de la iglesia"),
        ("AC_ORIENTAR", "Orientar y apoyar a conversos y menos activos"),
        ("AC_LIMPIEZA", "Apoyar en la limpieza de la capilla"),
        ("AC_HOGAR", "Hacer noches de hogar"),
    ]

    CONVERSOS = [
        ("CV_ARBOL", "Trabajar en su árbol familiar"),
        ("CV_TEMPLO", "Ir al templo"),
        ("CV_HOGAR", "Hacer noches de hogar"),
        ("CV_ACTIVIDADES", "Participar en actividades de la iglesia"),
        ("CV_DOMINGOS", "Llegar todos los domingos según posibilidades"),
        ("CV_EDUCACION", "Programas BYU / Becas / FPE / Mentors"),
        ("CV_CLASES", "Aprender a dar clases"),
    ]

    QUORUM_SOCSOC = [
        ("QS_AUTOSUFICIENCIA", "Participar en autosuficiencia"),
        ("QS_BAUTIZOS_JOVENES", "Acompañar a jóvenes en bautizos del templo"),
        ("QS_ORDENANZAS", "Hacer ordenanzas mayores tras 1 año"),
    ]

    JOVENES = [
        ("JOV_LEMA", "Aprenderse el lema de HJ/MJ"),
    ]

    INVESTIGADORES = [
        ("INV_LIBRO_MORMON", "Leer el Libro de Mormón"),
        ("INV_ESCRITURAS", "Leer las escrituras"),
        ("INV_DOMINGOS3", "Asistir a 3 domingos consecutivos"),
        ("INV_ACTIVIDADES", "Participar en actividades del barrio"),
        ("INV_AMIGO", "Hacerse de un amigo"),
        ("INV_TEMPLO", "Ir al templo"),
    ]

    class Meta:
        managed = False   # No crea tabla
        verbose_name = "Meta"
        verbose_name_plural = "Metas"


# ============================================
#              MODELO OBRA MISIONAL
# ============================================
class ObraMisional(models.Model):

    ORGANIZACIONES = [
        ("QUORUM", "Quórum de Élderes"),
        ("SOCSOC", "Sociedad de Socorro"),
        ("HOMBRES", "Hombres Jóvenes"),
        ("MUJERES", "Mujeres Jóvenes"),
        ("PRIMARIA", "Primaria"),
    ]

    CONDICIONES = [
        ("MENOS_ACTIVOS", "Menos activos"),
        ("ACTIVOS", "Activos"),
        ("CONVERSOS", "Conversos"),
        ("INVESTIGADORES", "Investigadores"),
    ]

    ORDENANZAS = [
        ("BAUTISMO", "Bautismo"),
        ("INVESTIDURA", "Investidura"),
        ("SELLAMIENTO", "Sellamiento"),
    ]

    # ✔ Ningún campo obligatorio, todos pueden ser NULL
    organizacion = models.CharField(max_length=20, choices=ORGANIZACIONES, null=True, blank=True)
    condicion_actual = models.CharField(max_length=20, choices=CONDICIONES, null=True, blank=True)
    nombre = models.CharField(max_length=120, null=True, blank=True)
    meta = models.CharField(max_length=50, null=True, blank=True)
    ordenanza_faltante = models.CharField(max_length=50, choices=ORDENANZAS, null=True, blank=True)
    fecha_meta = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre or "Sin nombre"

