from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    now=datetime.now().strftime('')
    return HttpResponse(f'Hello world, la fecha del servidor es: {now}')

def lista_ordenada(request):
    numeros=request.GET['numeros']
    lista=numeros.split(',')
    lista=list(map(int,lista))
    lista.sort()
    numeros="la lista ordenada es: ["
    for valor in lista:
        numeros+=f"{valor},"
    else:
        numeros+="]"
    data={
        'status':'OK',
        'numeros': lista,
        'message': 'Lista ordenada correctamente',
    }
    return HttpResponse(
        json.dumps(data,indent=4),
        content_type="application/json"
    )

def saludar(request,name):
    mensaje=f"Hola, bienvenido {name}"
    return HttpResponse(mensaje)