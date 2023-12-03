from django.shortcuts import render, redirect
from .models import Usuario, Corretor
from .forms import UsuarioForms , CorretorForms

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
    if request.method == 'GET':
        form = CorretorForms()
        return render(request, 'cliente.html', {'form' : form})
    
    if request.method == 'POST': 
        form = CorretorForms(request.POST)
        
        if form.is_valid(): 
            form.save()
            return redirect('/') 
        

def ver_corretores(request):
     corretores = {
        'corretores' : Corretor.objects.all()
    }
     
    
     return render(request, 'corretores.html', corretores)



def edituser(request, id):
    usuario = Usuario.objects.filter().get(id=id)
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        email = request.POST.get('email')

        usuario.nome = nome
        usuario.idade = idade
        usuario.email = email

        usuario.save()
        return redirect('/usuarios')
    else:
        return render(request, 'edituser.html' ,{'usuario': usuario})
    


def deleteuser(request, id):
    usuario = Usuario.objects.filter().get(id=id)
    
    if request.method == 'GET':
        usuario.delete()
        return redirect('/usuarios')
    