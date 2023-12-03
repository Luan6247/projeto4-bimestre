from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('usuarios/', views.usuarios, name = 'listagem_usuarios'),
    path('cadastro-de-clientes', views.clienteview), # Chama a view de cliente
    path('cadastro-de-corretores', views.corretorview),
    path('view_corretores', views.ver_corretores),
    path('editar_usuario/<int:id>/',  views.edituser, name='editar_usuario'),
    path('deletar_usuario/<int:id>/', views.deleteuser, name='deletar_usuario'),
    path('editar_corretor/<int:id>/',  views.editcorretor, name='editar_corretor'),
    path('deletar_corretor/<int:id>/', views.deletecorretor, name='deletar_corretor'),
    path('contrato',  views.contrato, name='contrato'),
    path('novo_contrato', views.novo_contrato, name='novo_contrato'),
    path('editar_contrato/<int:id>/',  views.editcontrato, name='editar_contrato'),
    path('deletar_contrato/<int:id>/', views.deletecontrato, name='deletar_contrato'),
    path('imovel', views.imovel, name='imovel'),
    path('novo_imovel', views.novo_imovel, name='novo_imovel'),
    path('editar_imovel/<int:id>/',  views.editimovel, name='editar_imovel'),
    path('deletar_imovel/<int:id>/', views.deleteimovel, name='deletar_imovel')

]