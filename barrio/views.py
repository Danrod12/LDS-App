from .forms import ObraMisionalForm
from .models import *
from django.shortcuts import render, redirect
from .serializers import *
from rest_framework import viewsets


class ObraMisionalViewSet(viewsets.ModelViewSet):
    queryset = ObraMisional.objects.all()
    serializer_class = ObraMisionalSerializer


def dashboard(request):
    obras = ObraMisional.objects.all()

    if request.method == 'POST':
        form = ObraMisionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # se actualiza la página
    else:
        form = ObraMisionalForm()

    return render(request, 'dashboard.html', {
        'form': form,
        'obras': obras
    })
    

def obispado(request):
    obras = ObraMisional.objects.all()
    return render(request, 'obispado.html', {'obras': obras})

def quorum(request):
    obras = ObraMisional.objects.all()
    return render(request, 'quorum.html', {'obras': obras})

def socsoc(request):
    return render(request, "socsoc.html")

def hjovenes(request):
    obras = ObraMisional.objects.all()
    return render(request, 'hjovenes.html', {'obras': obras})

def mjovenes(request):
    obras = ObraMisional.objects.all()
    return render(request, 'mjovenes.html', {'obras': obras})

def primaria(request):
    obras = ObraMisional.objects.filter(organizacion='PRIMARIA')
    return render(request, 'primaria.html', {'obras': obras})
