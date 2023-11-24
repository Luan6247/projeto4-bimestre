from django.shortcuts import render
from .models import Usuario

def login(request):
    return render(request, 'index.html')
def usuarios(request):
    print(request.POST.get('nome'), request.POST.get('idade'))
    novo_usuario = Usuario(nome = request.POST.get('nome'), idade = request.POST.get('idade'))
    #novo_usuario.nome = request.POST.get('nome')
    #novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios.html', usuarios)