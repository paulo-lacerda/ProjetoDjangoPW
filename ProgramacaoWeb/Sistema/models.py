from django.db import models

class Usuario(models.Model):
    login = models.CharField(max_length=100, null = False)
    senha = models.CharField(max_length=100, null = False)
    nome = models.CharField(max_length=100, null = False)
    telefone = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
class Distribuidor(models.Model):
    nome = models.CharField(max_length=100, null = False)
    cnpj = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100, null = False)
    distribuidor=models.ForeignKey(Distribuidor)
    quantidade = models.IntegerField(null = False)
    precoCusto = models.CharField(max_length=100)
    precoVenda = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
        
class Cliente(models.Model):
    nome = models.CharField(max_length=100, null = False)
    cpf = models.CharField(max_length=100, null = False)
    nome = models.CharField(max_length=100, null = False)
    
    def __str__(self):
        return self.nome