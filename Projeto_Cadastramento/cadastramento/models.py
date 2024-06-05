from django.db import models

# Modelo representando Lojistas
class Lojistas(models.Model):
    nome = models.CharField(max_length=75)
    data = models.CharField(max_length=10)
    tel = models.CharField(max_length=14)
    cpf = models.CharField(max_length=15)
    email = models.EmailField()
    senha = models.CharField(max_length=64)

    class Meta:
        # Nome singular para o modelo no admin
        verbose_name = 'Lojista'

    def __str__(self) -> str:
        # Representação textual do objeto
        return self.nome

# Modelo representando Lojas
class Lojas(models.Model):
    nome = models.CharField(max_length=75)
    endereco = models.CharField(max_length=10)
    tel = models.CharField(max_length=14)
    cnpj = models.CharField(max_length=14)
    pagamento = models.CharField(max_length=75)
    descricao = models.TextField()
    senha = models.CharField(max_length=64)

    class Meta:
        # Nome singular para o modelo no admin
        verbose_name = 'Loja'

    def __str__(self) -> str:
        # Representação textual do objeto
        return self.nome

# Modelo representando Produtos
class Produtos(models.Model):
    nome = models.CharField(max_length = 50)
    codigo_da_roupa = models.CharField(max_length = 10)
    imagem_produto = models.ImageField(upload_to='img_produtos/')
    preco = models.DecimalField((""), max_digits=5, decimal_places=2)
    descricao = models.TextField()
    numero_produtos_inicial = models.IntegerField()

    class Meta:
        # Nome singular para o modelo no admin
        verbose_name = 'Produto'

    def __str__(self) -> str:
        # Representação textual do objeto
        return self.nome
