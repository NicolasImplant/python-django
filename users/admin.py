from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Importamos la clase profile
from users.models import Profile
from posts.models import Post

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

    # Generamos la visualización del perfil desde admin
    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),)
        }),('Extra_info', {
            'fields': (
                ('webside', 'phone_number'),
                ('biography')
            ),
        }),('Metadata',{
            'fields': (('created', 'modified'),),
        })
    )
    # Se debe añadir la variable 'readonly_fields' ya que estos campos no se pueden ni deben editar desde el perfil de admin
    readonly_fields = ('created', 'modified',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin profile view"""

    list_display = ('pk', 'user', 'title', 'photo')
    list_display_links = ('pk', 'user')
    list_filter = ('created', 'modified')
    readonly_fields = ('created', 'modified')



class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


