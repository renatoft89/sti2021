from django.db import models
from nobreaks.models import Nobreak
from setores.models import Setor
from impressoras.models import Impressora
from usuarios.models import Usuario
from multiselectfield import MultiSelectField

MEMORIA_CHOICES = [
    ("2GB", "2GB"),
    ("4GB", "4GB"),
    ("6GB", "6GB"),
    ("8GB", "8GB"),
    ("12GB", "12GB"),
]

PROCESSADOR_CHOICES = [
    ("Dual Core", "Dual Core"),
    ("intel I3", "intel I3"),
    ("intel I5", "intel I5"),
    ("intel I7", "intel I7"),
]

WINDOWS_CHOICES = [
    ("1", "Windows Xp"),
    ("2", "Windows 7"),
    ("3", "Windows 8"),
    ("4", "Windows 10"),
    ("5", "Linux"),
]

NET_CHOICES = [
    ("1", "Rj45"),
    ("2", "Wi-Fi"),

]
ANTVIR_CHOICES = [
    ("KSP", "Kaspersky"),
    ("KSF", "Kaspersky Free"),
    ("AVS", "Avast"),
    ("OUT", "Outro"),

]

OFFICE_CHOICES = [
    ("1", "Office 2007"),
    ("2", "Office 2010"),
    ("3", "Office 2013"),
    ("4", "Office 2016"),

]
CON_IMPRE_CHOICES = [
    ("1", "Wi_Fi"),
    ("2", "RJ-45"),
    ("3", "Wi_Fi"),
]
MODEL_MAQ_CHOICES = [
    ("1", "HP402"),
    ("2", "Pro One"),
    ("3", "Itautec"),
]
TP_EQUIPAMENTOS = [
    ("1", "Computador"),
    ("2", "Impressora"),
    ("3", "Nobreak")
]

class Maquina(models.Model):
    
    
    patrimonio = models.CharField(max_length=6, unique=True)

    usuario = models.ForeignKey(
        Usuario, null=True, blank=True, on_delete=models.PROTECT
    )

    grupo = models.ForeignKey(
        Setor, null=True, blank=True, on_delete=models.PROTECT
    )

    modelo = models.CharField(max_length=14, choices=MODEL_MAQ_CHOICES)

    sistema = models.CharField(max_length=10, choices=WINDOWS_CHOICES)
    memoria = models.CharField(max_length=5, choices=MEMORIA_CHOICES)

    host = models.CharField(max_length=30, unique=True)
    processador = models.CharField(max_length=10, choices=PROCESSADOR_CHOICES)

    office = models.CharField(max_length=10, choices=OFFICE_CHOICES)
    antivirus = models.CharField(max_length=30, choices=ANTVIR_CHOICES)

    nobreak = models.ForeignKey(
        Nobreak, null=True, blank=True, on_delete=models.PROTECT
    )
    internet = models.CharField(max_length=4, choices=NET_CHOICES)

    impressora = models.ForeignKey(
        Impressora, null=True, blank=True, on_delete=models.PROTECT
    )
    conexao_impressora = models.CharField(max_length=6, choices=CON_IMPRE_CHOICES)
    ocs = models.CharField(max_length=3)
    observacao = models.TextField()

    def __str__(self):
        return self.usuario