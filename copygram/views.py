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

# Función para generar una nueva vista, el usuaruio ingresará información en el endpoint y esta informació se regresa en pantalla en formato JSON
def sorted_integers(request):
    """Return sorted integer list in a JSON object"""
    numbers = map(lambda x: int(x), request.GET['numbers'].split(','))
    return JsonResponse(
        {'Status'  : 'Ok',
         'Numbers' : sorted(numbers),
         'Message' : 'Integer sorted succesfully'}, json_dumps_params={'indent' : 1})

# Función para validar el nombre y la edad del usuario, si la edad del usuario es menor a 13 años debe generar un mensaje de alerta.
def say_hi(request, name, age):
    """Return a greeting and validate user data"""
    if age < 13:
        message = f'Sorry, if you have only {age} years old, your are not allowed here'
    else:
        message = f'Hello {name}, welcome to copygram'
        
    return HttpResponse(message) 