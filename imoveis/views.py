from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForms

def login(request):
    return render(request, 'login.html')

def usuarios(request):
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios.html', usuarios)

def clienteview(request): # Para renderizar a página
    if request.method == 'GET': # Se o usuário estiver apenas acessando a url
        form = UsuarioForms()
        return render(request, 'cliente.html', {'form' : form})
    
    if request.method == 'POST': # Se o usuárioj estiver enviando um formulário
        form = UsuarioForms(request.POST)
        
        if form.is_valid(): # Se o formulário for válido
            form.save()
            return redirect('/') # Redireciona para a página principal

def corretorview(request):
    return render(request, 'corretor.html')