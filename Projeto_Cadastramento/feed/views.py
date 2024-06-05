from django.shortcuts import render
from cadastramento.models import Produtos

# View para renderizar a página do feed
def feed_produtos(request):
    # Buscar todos os produtos cadastrados
    produtos = Produtos.objects.all()

    # Criar uma lista para armazenar os dados dos produtos
    feed_data = []

    # Iterar sobre os produtos para obter informações
    for produto in produtos:
        feed_data.append({
            'imagem_produto': produto.imagem_produto,
            'nome': produto.nome,
            'preco': produto.preco
        })

    # Passar os dados para o template e renderizá-lo
    return render(request, 'feed.html', {'feed_data': feed_data})

