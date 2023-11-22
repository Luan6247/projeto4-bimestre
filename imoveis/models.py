from django.db import models

class Imovel(models.Model):
    proprietario = models.CharField(max_length=50, blank=False)
    inquilino = models.CharField(max_length=50, blank=False)
    ContratoAluguel = models.DateField(blank=False)