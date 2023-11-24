from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('usuarios/', views.usuarios, name = 'listagem_usuarios')
]