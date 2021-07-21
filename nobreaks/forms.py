from django.forms import ModelForm
from .models import Nobreak

class NobreakForm(ModelForm):
    class Meta:
        model = Nobreak
        fields = ['patrimonio', 'modelo_nobreak']