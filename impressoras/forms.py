from django.forms import ModelForm
from .models import Impressora

class ImpressoraForm(ModelForm):
    class Meta:
        model = Impressora
        fields = ['patrimonio', 'modelo', 'mac', 'ip_impressora']