from django.contrib import admin
from .models import Lojistas, Lojas, Produtos

# Registro dos modelos no admin
admin.site.register(Lojistas)
admin.site.register(Lojas)
admin.site.register(Produtos)
