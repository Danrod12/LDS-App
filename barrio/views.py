from .forms import *
from .models import *
from django.shortcuts import render, redirect
from .serializers import *
from rest_framework import viewsets
from django.shortcuts import get_object_or_404, redirect


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


def marcar_completado(request, obra_id):
    obra = get_object_or_404(ObraMisional, id=obra_id)

    # Si el checkbox está marcado en el formulario → "done" aparece en POST
    obra.done = 'done' in request.POST
    obra.save()

    # Regresa exactamente a la página previa
    return redirect(request.META.get('HTTP_REFERER', '/'))


# def login_view(request):
#     error = None

#     if request.method == "POST":
#         form = LoginForm(request.POST)

#         if form.is_valid():
#             pin = form.cleaned_data["pin"]

#             # Buscar si existe un pin válido en la DB
#             try:
#                 user = LoginUser.objects.get(pin=pin)

#                 # REDIRECCION SEGÚN ORGANIZACION
#                 return redirect(user.organizacion.lower())

#             except LoginUser.DoesNotExist:
#                 error = "PIN incorrecto"

#     else:
#         form = LoginForm()

#     return render(request, "login.html", {"form": form, "error": error})

