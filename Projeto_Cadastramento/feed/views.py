from django.shortcuts import render, get_object_or_404
from cadastramento.models import Produtos, Lojas


# View para renderizar a página do feed de uma loja específica
def feed_produtos_loja(request, loja_id):
    loja = get_object_or_404(Lojas, id=loja_id)
    
    feed_data = []

    produtos = Produtos.objects.filter(loja=loja)

    for produto in produtos:
        feed_data.append({
            'imagem_produto': produto.imagem_produto,
            'nome': produto.nome,
            'preco': produto.preco
        })
    
    return render(request, 'feed.html', {'feed_data': feed_data, 'loja': loja})

def feed_geral(request):
    query = request.GET.get('q', '')

    feed_data = []

    if query:
        produtos = Produtos.objects.filter(nome__icontains=query)
    else:
        produtos = Produtos.objects.all()

    for produto in produtos:
        feed_data.append({
            'imagem_produto': produto.imagem_produto,
            'nome': produto.nome,
            'preco': produto.preco,
            'loja': produto.loja.nome  
        })
    
    return render(request, 'inicio.html', {'feed_data': feed_data})

