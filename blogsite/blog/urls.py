from django.urls import path
from . import views #. is the current dir. Views is the file views.py
from .views import PostListView #import the class PostListView from views.py


##########################this is the blog app level urls.py file####################

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'), #empty path is the default. PostListView.as_view() returns the HTTP response name is the name of the route.
    path('about/', views.about, name='blog-about'), #path is /about. Views.about returns the HTTP response. Name is the name of the route.
    path("blog/<int:pk>", views.view_blog, name = "view_blog" ), #path is /blog/<int:pk>. Views.view_blog returns the HTTP response. Name is the name of the route.
]