from django.db import models

class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ("A", "Alta",),
        ("N", "Normal"),
        ("B", "Baixa"),
    ]
    titulo = models.CharField(max_length=30, null=False, blank= False)
    descricao = models.CharField(max_length=100, blank=False, null=False)
    data_espiracao = models.DateField(null=False, blank= False)
    prioridade = models.CharField(max_length=1, choices=PRIORIDADE_CHOICES, null=False, blank=False)
