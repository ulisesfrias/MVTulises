from django.shortcuts import render
from django.http import HttpResponse
from MVT_entrega.models import familia 


# Create your views here.

def listado_de_familia(request):
    listado = familia.objects.all()

    Vista = ""
    for FAMILIA in listado:
        Vista += f"({FAMILIA.nombres},{FAMILIA.edad})" + " | "

    return HttpResponse(Vista)