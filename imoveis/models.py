from django.db import models

class Imovel(models.Model):
    nome = models.CharField(max_length=255, null=True)
    endereco = models.TextField(null=True)
    proprietario = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING)
    ContratoAluguel = models.ForeignKey('Contrato',  on_delete=models.CASCADE)
    imagem = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nome
    
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=150, null=True)
    idade = models.IntegerField(null=True)
    
    def __str__(self):
        return self.nome
    
class Corretor(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    numero = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nome

class Contrato(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=True)
    tipo_contrato = models.CharField(max_length = 255, choices = [("aluguel", "aluguel"), ("Venda", "Venda")])
    data = models.DateField()
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    cliente = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING)
    corretor = models.ForeignKey('Corretor', on_delete=models.CASCADE)
    
    def __str__(self):
      return  self.nome