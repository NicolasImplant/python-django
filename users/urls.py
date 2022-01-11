from django.urls import path
from users import views

urlpatterns = [

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
        view  = views.SignupView.as_view(),
        name  = 'Signup',
        ),

    path(
        route = 'me/profile',
        view  = views.UpdateProfileView.as_view(),
        name  = 'Update_profile',
        ),

    # Posts

    path(
        route = '<str:username>/',
        view  = views.UserDetailView.as_view(),
        name  = 'detail'
        ),
]