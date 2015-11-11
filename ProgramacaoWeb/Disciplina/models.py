from django.db import models
import Aluno

# Create your models here.

class Disciplina(models):
    nome = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=500)
    alunos = models.ForeignKey(Aluno.models.Aluno)