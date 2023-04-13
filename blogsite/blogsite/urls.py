from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls), #this is the path to the admin site
    path('', include('blog.urls')), #this is the path to the blog app level urls.py file
    path("user/", include('users.urls')), #this is the path to the users app level urls.py file
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)