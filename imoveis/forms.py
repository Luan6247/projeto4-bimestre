from django.forms import ModelForm
from .models import Usuario

class UsuarioForms(ModelForm): # Formulário gerado automaticamente.
    class Meta:
        model = Usuario
        fields = ['nome', 'idade']