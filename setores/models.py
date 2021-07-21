from django.db import models
from multiselectfield import MultiSelectField

LOCAL_CHOICES = [
    ("Subsolo", "Subsolo"),
    ("Térreo", "Térreo"),
    ("1º Andar", "1º Andar"),
    ("2º Andar", "2º Andar"),
    ("3º Andar", "3º Andar"),
]

class Setor(models.Model):
    nome_setor = models.CharField(max_length=30, unique=True)
    localizacao = models.CharField(max_length=8, choices=LOCAL_CHOICES)
    grupo = models.CharField(max_length=30)


    def __str__(self):
        return self.nome_setor