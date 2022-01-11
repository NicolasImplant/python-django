from django.urls import path
from posts import views


urlpatterns = [

    path(
        route = '',
        view  = views.PostsFeedView.as_view(),
        name='Feed',
        ),

    path(
        route = 'posts/new',
        view  = views.create_post,
        name  = 'New_Post'
        ),

    

    
    
]