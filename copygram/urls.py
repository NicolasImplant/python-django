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

from django.contrib import admin
from django.urls import path
from copygram import settings, views as local_views
from posts import views as posts_views
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/', local_views.hello_world, name='Hello_World'),
    path('sorted/', local_views.sorted_integers, name='Sort'),
    path('hi/<str:name>/<int:age>/', local_views.say_hi, name='Hi'),
    path('', posts_views.list_posts, name='Feed'),
    path('posts/new', posts_views.create_post, name='New_Post'),
    path('users/login', user_views.login_view, name='Login' ),
    path('users/logout', user_views.logout_view, name='Logout' ),
    path('users/signup', user_views.signup, name='Signup' ),
    path('users/me/profile', user_views.update_profile, name='Update_profile'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
