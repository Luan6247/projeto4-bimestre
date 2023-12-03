from django.forms import ModelForm
from .models import Usuario, Corretor, Contrato

class UsuarioForms(ModelForm): # Formulário gerado automaticamente.
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'idade']


class CorretorForms(ModelForm): # Formulário gerado automaticamente.
    class Meta:
        model = Corretor
        fields = ['nome', 'cpf', 'numero']


class ContratoForms(ModelForm):
    class Meta:
        model = Contrato
        fields = ['nome', 'tipo_contrato', 'data', 'valor', 'cliente', 'corretor' ]
