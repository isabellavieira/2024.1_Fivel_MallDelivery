# cadastramento/models.py

from django.db import models

class Lojistas(models.Model):
    nome = models.CharField(max_length=75)
    data = models.CharField(max_length=10)
    tel = models.CharField(max_length=14)
    cpf = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Lojista'

    def __str__(self) -> str:
        return self.nome

class Lojas(models.Model):
    lojista = models.ForeignKey(Lojistas, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=75)
    endereco = models.CharField(max_length=100)
    tel = models.CharField(max_length=14)
    cnpj = models.CharField(max_length=18)
    pagamento = models.CharField(max_length=75)
    descricao = models.TextField()
    senha = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Loja'

    def __str__(self) -> str:
        return self.nome

class Produtos(models.Model):
    loja = models.ForeignKey(Lojas, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=50)
    codigo_da_roupa = models.CharField(max_length=10)
    imagem_produto = models.ImageField(upload_to='img_produtos/')
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField()
    numero_produtos_inicial = models.IntegerField()

    class Meta:
        verbose_name = 'Produto'

    def __str__(self) -> str:
        return self.nome
