from django.db import models

class Imovel(models.Model):
    nome = models.CharField(max_length=255)
    proprietario = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING)
    ContratoAluguel = models.ForeignKey('Contrato',  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    
    def __str__(self):
        return self.nome
    
class Corretor(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

class Contrato(models.Model):
    nome = models.CharField(max_length=255)
    tipo_contrato = models.CharField(max_length = 255, choices = [("aluguel", "aluguel"), ("Venda", "Venda")])
    data = models.DateField()
    valor = models.DecimalField(max_digits=19, decimal_places=10)
    cliente = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING)
    corretor = models.ForeignKey('Corretor', on_delete=models.CASCADE)
    
    def __str__(self):
        self.nome