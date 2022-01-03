from django.contrib import admin
# Importamos la clase profile
from users.models import Profile

# Register your models here.

# Creamos la clase profile admin para la visualizacion de administrador
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    # Definimos la manera en que los usuarios admin visualizarán los perfiles
    list_display = ('pk', 'user', 'phone_number', 'webside', 'picture')
    # Generamos links al detalle de usuario
    list_display_links = ('pk', 'user')
    # Habilitamos la posibilidad de editar desde la visualizacion principal, los datos no pueden ser link y ser editables al mismo tiempo
    list_editable =('phone_number', 'webside', 'picture')
    # Generar una area de busqueda para movernos de manera rapida entre los perfiles, debemos especificar que argumentos son validos para la busqueda
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'user__username')
    # Añadimos un filtro de usuarios por fecha de creación o modificación del perfil, si está activo o si es parte del staff
    # el orden de declaración será el orden en el que apareceran en la interfaz
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')

