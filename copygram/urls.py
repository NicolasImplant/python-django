"""copygram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


""" Copygram Url's modeule."""


from django.urls import path
# Importamos la clase HttpResponse para generar la respuesta del primer "Hola-Mundo"
from django.http import HttpResponse

# Función para imprimir en pantalla una respuesta HTTP personalizada
def hello_world(request):
    """Return a greeting"""
    return HttpResponse('¡ Hello world from Django and python !')

urlpatterns = [
    path('hello_world/', hello_world),
]
