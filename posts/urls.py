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
        view  = views.CreatePostView.as_view(),
        name  = 'New_Post'
        ),

    path(
        route = 'posts/<int:pk>/',
        view  = views.PostDetailView.as_view(),
        name  = 'detail' 
    )     
    
]