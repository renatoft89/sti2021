from django.db import models
from setores.models import Setor

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=30)
    usuario_sistema = models.CharField(max_length=30, unique=True)
    setor_usuario = models.ForeignKey(
        Setor, null=True, blank=True, on_delete=models.PROTECT
)
    def __str__(self):
        return self.nome_completo


    
    
    