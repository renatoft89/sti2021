from django.db import models
from multiselectfield import MultiSelectField



MODEL_CHOICES = [
    ("Epson L455", "Epson L455"),
    ("HP 2055dn", "HP 2055dn"),
    ("HP 2015", "HP 2015"),
    ("HP 1200", "HP 1200"),
    ("HP j2010", "HP j2010"),
    ("HP M201", "HP M201"),
    ("HP DESKJET 2546", "HP DESKJET 2546"),
    ("HP CM1410", "HP CM1410"),
    ("HP DESKJET 895", "HP DESKJET 895"),
    ("HP PRO400", "HP PRO400")

    
]

class Impressora(models.Model):
    patrimonio = models.CharField(max_length=6, unique=True)
    modelo = models.CharField(max_length=16, choices=MODEL_CHOICES)
    mac = models.CharField(max_length=17, unique=True)
    ip_impressora = models.CharField(max_length=16, unique=True)
    
    def __str__(self):
        return self.patrimonio+ ' ' + self.modelo