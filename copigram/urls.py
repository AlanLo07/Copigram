"""copigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from copigram import views as local_views
from posts import views as posts_views
from users import views as user_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', local_views.hello_world, name='hello_world'),
    path('numeros/',local_views.lista_ordenada, name='sort'),
    path('saludar/<str:name>/', local_views.saludar,name='hi'),
    path('posts/',posts_views.list_posts,name='feed'),
    path('users/login/',user_views.login_view,name='login'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
