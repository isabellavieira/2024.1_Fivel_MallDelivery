from django.db import models


class Lojistas(models.Model):
    nome = models.CharField(max_length=75)
    data = models.CharField(max_length=10)
    tel = models.CharField(max_length=14)
    cpf = models.CharField(max_length=15)
    email = models.EmailField()
    senha = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Lojista'

    def __str__(self) -> str:
        return self.nome


class Lojas(models.Model):
    nome = models.CharField(max_length=75)
    endereco = models.CharField(max_length=10)
    tel = models.CharField(max_length=14)
    cnpj = models.CharField(max_length=14)
    pagamento = models.CharField(max_length=75)
    descricao = models.TextField()
    senha = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Loja'

    def __str__(self) -> str:
        return self.nome


class Produtos(models.Model):
    nome = models.CharField(max_length = 50)
    codigo_da_roupa = models.CharField(max_length = 5)
    imagem_produto = models.ImageField()
    preco = models.FloatField()  
    descricao = models.TextField()
    numero_produtos_inicial = models.IntegerField()

    class Meta:
        verbose_name = 'Produto'

    def __str__(self) -> str:
        return self.nome