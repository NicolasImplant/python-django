from django.urls import path
from users import views

urlpatterns = [

    # Posts

    path(
        route = '<str:username>/',
        view  = views.UserDetailView.as_view(),
        name  = 'detail'
        ),


    # Management
    path(
        route = 'login',
        view  = views.login_view,
        name  = 'Login',
        ),

    path(
        route = 'logout',
        view  = views.logout_view,
        name  = 'Logout',
        ),

    path(
        route = 'signup',
        view  = views.signup,
        name  = 'Signup',
        ),

    path(
        route = 'me/profile',
        view  = views.update_profile,
        name  = 'Update_profile',
        ),
]