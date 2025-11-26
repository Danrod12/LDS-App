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


# ============================================
#                 DASHBOARD
# ============================================
def dashboard(request):
    obras = ObraMisional.objects.all()

    if request.method == 'POST':
        form = ObraMisionalForm(request.POST)
        if form.is_valid():
            form.save()
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
def obispado(request):
    obras = ObraMisional.objects.all()
    return render(request, 'obispado.html', {'obras': obras})


def quorum(request):
    obras = ObraMisional.objects.filter(organizacion='QUORUM')
    return render(request, 'quorum.html', {'obras': obras})


def socsoc(request):
    obras = ObraMisional.objects.filter(organizacion='SOCSOC')
    return render(request, 'socsoc.html', {'obras': obras})


def hjovenes(request):
    obras = ObraMisional.objects.filter(organizacion='HOMBRES')
    return render(request, 'hjovenes.html', {'obras': obras})


def mjovenes(request):
    obras = ObraMisional.objects.filter(organizacion='MUJERES')
    return render(request, 'mjovenes.html', {'obras': obras})


def primaria(request):
    obras = ObraMisional.objects.filter(organizacion='PRIMARIA')
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