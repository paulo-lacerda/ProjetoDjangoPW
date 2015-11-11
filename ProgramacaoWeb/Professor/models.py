from django.db import models
import Disciplina

# Create your models here.

class Professor(models):
    nome = models.CharField(max_length=100, null = False)
    disciplina = models.ForeignKey(Disciplina.models.Disciplina)