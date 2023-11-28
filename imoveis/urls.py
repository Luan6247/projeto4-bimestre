from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('usuarios/', views.usuarios, name = 'listagem_usuarios'),
    path('cadastro-de-clientes', views.clienteview), # Chama a view de cliente
    path('cadastro-de-corretores', views.corretorview) # Chama a view do corretor
]