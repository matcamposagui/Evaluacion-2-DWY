"""Evaluacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth import views as auth_views
from Evaluacion.views import index, nosotros, productos, registro
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('nosotros/', nosotros),
    path('productos/', productos),
    path('registro/', registro),
    #path('', LoginView.as_view(template_name="login.html")),
    path('', views.index, name='index'),
    path('login/', views.index, name='login')
]

urlpatterns+= [

    path('accounts/', include ('django.contrib.auth.urls')),


]
