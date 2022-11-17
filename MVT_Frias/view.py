from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime


def fecha_actual(request):
    hoy=datetime.now().strftime("%d|%m|%Y")
    return HttpResponse(f"Fecha actual: {hoy}")


def datos_familiares(request):

    archivo = open(r"C:\Users\ivo frias\Documents\CARPETA CODER\MVT_Frias\MVT_Frias\templates\mvt.html")

    #cramos el template y le pasamos el cont de archivo
    plantilla = Template(archivo.read())

    #cerramos archivo 
    archivo.close()

    informacion_nombre = ["Nombre: Ulises F",
     "Nombre: Ivo F.",
     "Nombre: Enzo F.",
     "Nombre: Ivana A.",
     "Nombre: Walter F."
    ]

    informacion_edad = ["Edad: 21",
    "Edad: 15",
    "Edad: 25",
    "Edad: 49",
    "Edad: 49"
    ]

    datos = {'informacion': informacion_nombre,'Edad': informacion_edad}

    #creamos el contexto
    contexto = Context(datos)

    #creamos el doc

    documento = plantilla.render(contexto)

    return HttpResponse(documento)