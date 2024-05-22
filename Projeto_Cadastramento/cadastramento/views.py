from django.shortcuts import render, redirect
from .models import Lojistas, Lojas
from hashlib import sha256


def inicio(request):
    return render(request, 'inicio.html')


def login_lojistas(request):
    status = request.GET.get('status')
    return render(request,'login_lojista.html', {'status': status})

def cadastrar_lojistas(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_lojista.html', {'status': status})

def validar_cadastro_lojistas(request):

    #Obtenção dos Dados do Formulário
    nome = request.POST.get('nome')
    data = request.POST.get('data')
    tel = request.POST.get('tel')
    cpf = request.POST.get('cpf')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    #Verificação de Email Existente
    lojista = Lojistas.objects.filter(email = email)

    #Verificação de Campos Vazios
    if len(nome.strip()) == 0 or len(data.strip()) == 0 or len(tel.strip()) == 0 or len(cpf.strip()) == 0 or len(email.strip()) == 0:
        return redirect('../cadastrar_lojistas/?status=1')
    
    #Verificação do Tamanho da Senha
    if len(senha) < 5:
        return redirect('../cadastrar_lojistas/?status=4')
    
    #Verificação de Email Duplicado
    if len(lojista) > 0:
        return redirect('../cadastrar_lojistas/?status=2')
    
    #Tentativa de Criação e Salvamento do Lojista
    try:
        senha = sha256(senha.encode()).hexdigest()
        lojistas = Lojistas(nome = nome, data = data, tel = tel, cpf = cpf, email = email, senha = senha)
        lojistas.save()
        return redirect('../cadastrar_lojistas/?status=0')

    except:
        return redirect('../cadastrar_lojistas/?status=3')

def validar_login_lojistas(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    lojista = Lojistas.objects.filter(email = email).filter(senha = senha)

    if len(lojista) == 0:
        return redirect('../login_lojistas/?status=1')
    elif len(lojista) > 0:
        request.session['lojista'] = lojista[0].id
        return redirect('../intermediaria1')
    

def intermediaria1(request):
    return render(request, 'intermediaria1.html')


def login_lojas(request):
    status = request.GET.get('status')
    return render(request,'login_loja.html', {'status': status})

def cadastrar_lojas(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_loja.html', {'status': status})

def validar_cadastro_lojas(request):

    #Obtenção dos Dados do Formulário
    nome = request.POST.get('nome')
    endereco = request.POST.get('endereco')
    tel = request.POST.get('tel')
    cnpj = request.POST.get('cnpj')
    pagamento = request.POST.get('pagamento')
    descricao = request.POST.get('descricao')
    senha = request.POST.get('senha')

    #Verificação de Nome Existente
    loja = Lojas.objects.filter(nome = nome)

    #Verificação de Campos Vazios
    if len(nome.strip()) == 0 or len(endereco.strip()) == 0 or len(tel.strip()) == 0 or len(cnpj.strip()) == 0 or len(pagamento.strip()) == 0 or len(descricao.strip()) == 0:
        return redirect('../cadastrar_lojas/?status=1')
    
    #Verificação do Tamanho da Senha
    if len(senha) < 5:
        return redirect('../cadastrar_lojas/?status=4')

    #Verificação de Email Duplicado
    if len(loja) > 0:
        return redirect('../cadastrar_lojas/?status=2')

    #Tentativa de Criação e Salvamento da Loja
    try:
        senha = sha256(senha.encode()).hexdigest()
        lojas = Lojas(nome = nome, endereco = endereco, tel = tel, cnpj = cnpj, pagamento = pagamento, descricao = descricao, senha = senha)
        lojas.save()
        return redirect('../cadastrar_lojas/?status=0')

    except:
        return redirect('../cadastrar_lojas/?status=3')

def validar_login_lojas(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    loja = Lojas.objects.filter(nome = nome).filter(senha = senha)

    if len(loja) == 0:
        return redirect('../login_lojistas/?status=1')
    elif len(loja) > 0:
        request.session['loja'] = loja[0].id
        return redirect('../home')
    

def sair(request):
    request.session.flush()
    return redirect('')