from django.shortcuts import render, redirect
from .models import Usuario, Corretor, Contrato, Imovel
from .forms import UsuarioForms , CorretorForms, ContratoForms, ImovelForms

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
    

def editcorretor(request, id):
    corretor = Corretor.objects.filter().get(id=id)
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf= request.POST.get('cpf')
        numero = request.POST.get('numero')

        corretor.nome = nome
        corretor.cpf = cpf
        corretor.numero = numero

        corretor.save()
        return redirect('/view_corretores')
    
    else:
        return render(request, 'editcorretor.html' ,{'corretor': corretor})
    

def deletecorretor(request, id):
    corretor = Corretor.objects.filter().get(id=id)
    
    if request.method == 'GET':
        corretor.delete()
        return redirect('/view_corretores')
    

def contrato(request):
    contratos = Contrato.objects.all()
    return render(request, 'contrato.html', {'contratos': contratos})



def novo_contrato(request):
    if request.method == 'GET': # Se o usuário estiver apenas acessando a url
        form = ContratoForms()
        return render(request, 'novocontrato.html', {'form' : form})
    
    if request.method == 'POST': # Se o usuárioj estiver enviando um formulário
        form = ContratoForms(request.POST)
        
        if form.is_valid(): # Se o formulário for válido
            form.save()
            return redirect('/contrato') # Redireciona para a página principal



def editcontrato(request, id):
    contrato = Contrato.objects.filter().get(id=id)
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        data = request.POST.get('data')
        valor = request.POST.get('valor')


        contrato.nome = nome
        contrato.data = data
        contrato.valor = valor

        contrato.save()
        return redirect('/contrato')
    
    else:
        return render(request, 'editcontrato.html' ,{'contrato': contrato})


def deletecontrato(request, id):
    contrato = Contrato.objects.filter().get(id=id)
    
    if request.method == 'GET':
        contrato.delete()
        return redirect('/contrato')
    

def imovel(request):
    imoveis = Imovel.objects.all()
    return render(request, 'imovel.html', {'Imoveis': imoveis})


def novo_imovel(request):
    if request.method == 'GET': # Se o usuário estiver apenas acessando a url
        form = ImovelForms()
        return render(request, 'novoimovel.html', {'form' : form})
    
    if request.method == 'POST': # Se o usuárioj estiver enviando um formulário
        form = ImovelForms(request.POST)
        
        if form.is_valid(): # Se o formulário for válido
            form.save()
            return redirect('/imovel')
        

def editimovel(request, id):
    imovel = Imovel.objects.filter().get(id=id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        imagem = request.POST.get('imagem')



        imovel.nome = nome
        imovel.endereco = endereco
        imovel.imagem = imagem

        imovel.save()
        return redirect('/imovel')
    
    else:
        return render(request, 'editimovel.html' ,{'imovel': imovel})



def deleteimovel(request, id):
    imovel = Imovel.objects.filter().get(id=id)

    if request.method == 'GET':
        imovel.delete()
        return redirect('/imovel')
    