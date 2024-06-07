from django.urls import path
from . import views

# Definição das rotas (URLs) e mapeamento para as views correspondentes
urlpatterns = [
    path('<int:loja_id>/', views.feed_produtos_loja, name='feed_produtos_loja')
]
