from django.shortcuts import render, get_object_or_404
from cadastramento.models import Produtos, Lojas

# View para renderizar a página do feed de uma loja específica
def feed_produtos_loja(request, loja_id):
    loja = get_object_or_404(Lojas, id=loja_id)
    
    produtos = Produtos.objects.filter(loja=loja)

    feed_data = []

    for produto in produtos:
        feed_data.append({
            'imagem_produto': produto.imagem_produto,
            'nome': produto.nome,
            'preco': produto.preco
        })
    
    return render(request, 'feed.html', {'feed_data': feed_data, 'loja': loja})




