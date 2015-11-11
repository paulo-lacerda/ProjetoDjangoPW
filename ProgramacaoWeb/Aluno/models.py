from django.db import models
import Disciplina

class Aluno(models.Model):
    nome = models.CharField(max_length=100, null = False)
    matricula = models.IntegerField(max_length=100, null = False)
    email = models.CharField(max_length=100, null = False)
    disciplina=models.ForeignKey(Disciplina.models.Disciplina)
    professorDisciplina = models.ForeignKey()