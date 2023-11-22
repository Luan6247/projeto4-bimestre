from django.conf import settings
from django.db import models
from django.utils import timezone

class Imovel(models.Model):
    proprietario = models.CharField(max_length=50, blank=False)
    inquilino = models.CharField(max_length=50, blank=False)
    ContratoAluguel = models.DateField(blank=False)