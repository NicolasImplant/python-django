"""Copygram views"""

# Importamos la clase HttpResponse para generar la respuesta del primer "Hola-Mundo"
from django.http import HttpResponse
from django.http import JsonResponse

# Importamos las utilidades
from datetime import datetime

# Función para imprimir en pantalla una respuesta HTTP personalizada
def hello_world(request):
    """Return a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'¡ Hello world from Django and python ! Current server time is: {now}')

# Función para generar una nueva vista
def hi(request):
    """Hi"""
    numbers = map(lambda x: int(x), request.GET['numbers'].split(','))
    return JsonResponse({'numbers' : sorted(numbers)}, json_dumps_params={'indent' : 4})