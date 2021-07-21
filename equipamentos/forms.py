from django.forms import ModelForm
from .models import Maquina

class MaquinaForm(ModelForm):
    class Meta:
        model = Maquina
        fields = ['usuario', "grupo", 'host', 'patrimonio', 'modelo', 'processador', 'memoria', 'sistema', 'office',
                  'usuario', 'antivirus', 'nobreak', 'internet', 'impressora', 'conexao_impressora', 'ocs',
                  'observacao']