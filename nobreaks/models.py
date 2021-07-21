from django.db import models
from multiselectfield import MultiSelectField

MODEL_CHOICES = [
    ("1", "RAGTECH 1200Va"),
    ("2", "APC 600Va")
    
]

class Nobreak(models.Model):
    patrimonio = models.CharField(max_length=30, unique=True)
    modelo_nobreak = models.CharField(max_length=3, choices=MODEL_CHOICES)

    def __str__(self):
        return self.patrimonio+ ' ' + self.modelo_nobreak