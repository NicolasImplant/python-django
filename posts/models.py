from django.db import models

# Create your models here.

# Creamos el modelo de usuario para interactuar con la base de datos
class User(models.Model):
    """User Model"""

    # models. _____ nos permite validar que los datos ingresados respondan a los patrones soportados

    # El atributo unique valida que el email de usuario sea unico en la base de datos
    email = models.EmailField(unique=True)

    # Definimos un tamaño maximo para la cantidad de caracteres que serán ingresados
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    # validar si el usuario tiene permiso de administrador
    is_admin = models.BooleanField(default=False)

    # El usuario es libre sobre si rellena el bio o no. 
    bio = models.TextField(blank=True)

    # Se define de esta manera ya que el usuario es libre de llenar este campo
    birthdate = models.DateField(blank=True, null=True)

    # En cuanto el usuario es creado en la base de datos se cargará la fecha de su creación
    created_at = models.DateTimeField(auto_now_add=True)

    # Va a guardar la fecha en la que se editó por ultima vez
    modified_at = models.DateTimeField(auto_now=True)

    # Ubicación de los usuarios

    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)

    def __str__(self):
        """Returns user email"""
        return self.email


