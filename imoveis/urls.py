from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('usuarios/', views.usuarios, name = 'listagem_usuarios'),
    path('cadastro-de-clientes', views.clienteview), # Chama a view de cliente
    path('cadastro-de-corretores', views.corretorview),
    path('view_corretores', views.ver_corretores),
    path('editar_usuario/<int:id>/',  views.edituser, name='editar_usuario'),
    path('deletar_usuario/<int:id>/', views.deleteuser, name='deletar_usuario')
]