from django.urls import path
from django.views.generic import TemplateView
from users import views

urlpatterns = [

    # Posts

    path(
        route = '<str:username>/',
        view  = TemplateView.as_view(template_name = 'users/detail.html'),
        name  = 'detail'
        ),


    # Management
    path(
        route = 'users/login',
        view  = views.login_view,
        name  = 'Login',
        ),

    path(
        route = 'users/logout',
        view  = views.logout_view,
        name  = 'Logout',
        ),

    path(
        route = 'users/signup',
        view  = views.signup,
        name  = 'Signup',
        ),

    path(
        route = 'users/me/profile',
        view  = views.update_profile,
        name  = 'Update_profile',
        ),
]