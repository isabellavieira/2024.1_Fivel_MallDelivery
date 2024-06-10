from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Lojistas, Lojas, Produtos
from hashlib import sha256
from django.http import HttpResponseForbidden
from django.http import JsonResponse

def inicio(request):
    return render(request, 'inicio.html')

def login_lojistas(request):
    status = request.GET.get('status')
    return render(request,'login_lojista.html', {'status': status})

def cadastrar_lojistas(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_lojista.html', {'status': status})

def validar_cadastro_lojistas(request):
    nome = request.POST.get('nome')
    data = request.POST.get('data')
    tel = request.POST.get('tel')
    cpf = request.POST.get('cpf')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    lojista = Lojistas.objects.filter(email=email)
    if len(nome.strip()) == 0 or len(data.strip()) == 0 or len(tel.strip()) == 0 or len(cpf.strip()) == 0 or len(email.strip()) == 0:
        return redirect('../cadastrar_lojistas/?status=1')
    if len(senha) < 5:
        return redirect('../cadastrar_lojistas/?status=4')
    if len(lojista) > 0:
        return redirect('../cadastrar_lojistas/?status=2')
    try:
        senha = sha256(senha.encode()).hexdigest()
        lojistas = Lojistas(nome=nome, data=data, tel=tel, cpf=cpf, email=email, senha=senha)
        lojistas.save()
        return redirect('../cadastrar_lojistas/?status=0')
    except:
        return redirect('../cadastrar_lojistas/?status=3')

def validar_login_lojistas(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()
    lojista = Lojistas.objects.filter(email=email).filter(senha=senha)
    if len(lojista) == 0:
        return redirect('../login_lojistas/?status=1')
    else:
        request.session['lojista'] = lojista[0].id
        return redirect('../intermediaria1')

def intermediaria1(request):
    return render(request, 'intermediaria1.html')

def login_lojas(request):
    status = request.GET.get('status')
    return render(request, 'login_loja.html', {'status': status})

def cadastrar_lojas(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_loja.html', {'status': status})

def validar_cadastro_lojas(request):
    nome = request.POST.get('nome')
    endereco = request.POST.get('endereco')
    tel = request.POST.get('tel')
    cnpj = request.POST.get('cnpj')
    pagamento = request.POST.get('pagamento')
    descricao = request.POST.get('descricao')
    senha = request.POST.get('senha')
    loja = Lojas.objects.filter(cnpj=cnpj)
    if len(nome.strip()) == 0 or len(endereco.strip()) == 0 or len(tel.strip()) == 0 or len(cnpj.strip()) == 0 or len(pagamento.strip()) == 0 or len(descricao.strip()) == 0:
        return redirect('../cadastrar_lojas/?status=1')
    if len(senha) < 5:
        return redirect('../cadastrar_lojas/?status=4')
    if len(loja) > 0:
        return redirect('../cadastrar_lojas/?status=2')
    try:
        senha = sha256(senha.encode()).hexdigest()
        lojista_id = request.session.get('lojista_id')
        lojista = get_object_or_404(Lojistas, id=lojista_id)
        loja = Lojas(lojista=lojista, nome=nome, endereco=endereco, tel=tel, cnpj=cnpj, pagamento=pagamento, descricao=descricao, senha=senha, status='pending')
        loja.save()
        return redirect('loja_em_analise')
    except Exception as e:
        print(e)
        return redirect('../cadastrar_lojas/?status=3')

def validar_login_lojas(request):
    cnpj = request.POST.get('cnpj')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()
    try:
        loja = Lojas.objects.get(cnpj=cnpj, senha=senha)
        request.session['loja_id'] = loja.id
        if loja.status == 'approved':
            return redirect(reverse('feed_produtos_loja', args=[loja.id]))
        else:
            return redirect('loja_em_analise')
    except Lojas.DoesNotExist:
        return redirect('../login_lojas/?status=1')

def cadastrar_produtos(request, loja_id):
    loja = get_object_or_404(Lojas, pk=loja_id)
    if loja.status != 'approved':
        return redirect('loja_em_analise')
    return render(request, 'cadastro_produtos.html', {'loja': loja})

def validar_cadastro_produtos(request, loja_id):
    nome = request.POST.get('nome')
    imagem_produto = request.FILES.get('imagem_produto')
    preco = request.POST.get('preco')
    descricao = request.POST.get('descricao')
    numero_produtos_inicial = request.POST.get('numero_produtos_inicial')
    loja = get_object_or_404(Lojas, pk=loja_id)
    produtos = Produtos(loja=loja, nome=nome, imagem_produto=imagem_produto, preco=preco, descricao=descricao, numero_produtos_inicial=numero_produtos_inicial)
    produtos.save()
    return redirect(reverse('feed_produtos_loja', args=[loja.id]))

def feed_produtos_loja(request, loja_id):
    loja = get_object_or_404(Lojas, id=loja_id)
    if loja.status != 'approved':
        return HttpResponseForbidden("Sua loja ainda não foi aprovada.")
    produtos = Produtos.objects.filter(loja=loja)
    feed_data = [{'imagem_produto': produto.imagem_produto, 'nome': produto.nome, 'preco': produto.preco} for produto in produtos]
    return render(request, 'feed.html', {'feed_data': feed_data, 'loja': loja})

def verificar_status_loja(loja_id):
    loja = get_object_or_404(Lojas, pk=loja_id)
    return JsonResponse({'status': loja.status})

def loja_em_analise(request):
    loja_id = request.session.get('loja_id')
    return render(request, 'loja_em_analise.html', {'loja_id': loja_id})


def feed_geral(request):
    query = request.GET.get('q', '')
    if query:
        produtos = Produtos.objects.filter(nome__icontains=query)
    else:
        produtos = Produtos.objects.all()

    return render(request, 'inicio.html', {'produtos': produtos})
