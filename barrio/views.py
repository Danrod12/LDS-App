from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import *
from .forms import ObraMisionalForm
from .serializers import ObraMisionalSerializer
from django.http import JsonResponse


# API REST
class ObraMisionalViewSet(viewsets.ModelViewSet):
    queryset = ObraMisional.objects.all()
    serializer_class = ObraMisionalSerializer

def crear_barrio(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        estaca = request.POST.get("estaca")

        barrio = Barrio.objects.create(
            nombre=nombre,
            estaca=estaca
        )

        return render(request, "crear_barrio.html", {
            "codigo": barrio.codigo
        })

    return render(request, "crear_barrio.html")



def login_barrio(request):
    if request.method == "POST":
        codigo = request.POST.get("codigo")

        try:
            barrio = Barrio.objects.get(codigo=codigo)

            # guardar en sesión
            request.session["barrio_id"] = barrio.id
            request.session["barrio_nombre"] = barrio.nombre

            return redirect("dashboard")

        except Barrio.DoesNotExist:
            return render(request, "login.html", {
                "error": "Código inválido"
            })

    return render(request, "login.html")
# ============================================
#                 DASHBOARD
# ============================================
def dashboard(request):
    barrio_id = request.session.get("barrio_id")

    if not barrio_id:
        return redirect("login_barrio")

    # 🔥 ahora solo del barrio activo
    obras = ObraMisional.objects.filter(barrio_id=barrio_id)

    if request.method == 'POST':
        form = ObraMisionalForm(request.POST)
        if form.is_valid():
            obra = form.save(commit=False)
            obra.barrio_id = barrio_id  # 🔗 clave del sistema
            obra.save()
            return redirect('dashboard')
    else:
        form = ObraMisionalForm()

    return render(request, 'dashboard.html', {
        'form': form,
        'obras': obras
    })

# ============================================
#      FILTROS POR ORGANIZACIÓN
# ============================================
def log(request):
    obras = ObraMisional.objects.filter(organizacion='LOP')
    return render(request, 'log.html', {'obras': obras})

def obispado(request):
    barrio_id = request.session.get("barrio_id")

    if not barrio_id:
        return redirect("login_barrio")

    obras = ObraMisional.objects.filter(barrio_id=barrio_id)

    return render(request, 'obispado.html', {'obras': obras})


def quorum(request):
    barrio_id = request.session.get("barrio_id")

    if not barrio_id:
        return redirect("login_barrio")

    obras = ObraMisional.objects.filter(barrio_id=barrio_id, organizacion='QUORUM')
    return render(request, 'quorum.html', {'obras': obras})


def socsoc(request):
    barrio_id = request.session.get("barrio_id")

    if not barrio_id:
        return redirect("login_barrio")

    obras = ObraMisional.objects.filter(barrio_id=barrio_id, organizacion='SOCSOC')
    return render(request, 'socsoc.html', {'obras': obras})


def hjovenes(request):
    barrio_id = request.session.get("barrio_id")

    if not barrio_id:
        return redirect("login_barrio")

    obras = ObraMisional.objects.filter(barrio_id=barrio_id, organizacion='HOMBRES')
    return render(request, 'hjovenes.html', {'obras': obras})


def mjovenes(request):
    barrio_id = request.session.get("barrio_id")

    if not barrio_id:
        return redirect("login_barrio")

    obras = ObraMisional.objects.filter(barrio_id=barrio_id, organizacion='MUJERES')
    return render(request, 'mjovenes.html', {'obras': obras})


def primaria(request):
    barrio_id = request.session.get("barrio_id")

    if not barrio_id:
        return redirect("login_barrio")

    obras = ObraMisional.objects.filter(barrio_id=barrio_id, organizacion='PRIMARIA')
    return render(request, 'primaria.html', {'obras': obras})


# ============================================
#             MARCAR COMPLETADO
# ============================================
def marcar_completado(request, obra_id):
    obra = get_object_or_404(ObraMisional, id=obra_id)
    obra.done = 'done' in request.POST
    obra.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))

def cargar_metas(request):
    condicion = request.GET.get("condicion")

    if condicion == "MENOS_ACTIVOS":
        metas = Meta.MENOS_ACTIVOS
    elif condicion == "ACTIVOS":
        metas = Meta.ACTIVOS
    elif condicion == "CONVERSOS":
        metas = Meta.CONVERSOS
    elif condicion in ["QUORUM", "SOCSOC"]:
        metas = Meta.QUORUM_SOCSOC
    elif condicion in ["HOMBRES", "MUJERES"]:
        metas = Meta.JOVENES
    elif condicion == "INVESTIGADORES":
        metas = Meta.INVESTIGADORES
    else:
        metas = []

    return JsonResponse(metas, safe=False)