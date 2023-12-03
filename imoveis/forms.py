from django.forms import ModelForm
from .models import Usuario, Corretor

class UsuarioForms(ModelForm): # Formulário gerado automaticamente.
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'idade']


class CorretorForms(ModelForm): # Formulário gerado automaticamente.
    class Meta:
        model = Corretor
        fields = ['nome', 'cpf', 'numero']


