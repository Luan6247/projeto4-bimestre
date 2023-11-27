from django.db import models

class Imovel(models.Model):
    proprietario = models.CharField(max_length=50)
    inquilino = models.CharField(max_length=50)
    ContratoAluguel = models.DateField()

class Usuario(models.Model):
    #id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()