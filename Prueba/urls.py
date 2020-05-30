"""Prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  fro  m other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.config.url.static import static

#from Prueba import views
#from Prueba.views import index, saludo

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'courses/', include('course.urls')),
    #path('saludo/', saludo),
    #path(r'courses/', views.index, name='index'),
] + static(settings.STATIC_UIRL, document_root=settings.STATIC_ROOT)