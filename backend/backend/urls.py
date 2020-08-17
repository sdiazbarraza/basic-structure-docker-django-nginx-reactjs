from django.urls import path

from . import views

urlpatterns = [
    path(r'test/', views.index, name='index'),
    path(r'test/prueba', views.prueba, name='prueba'),
]
