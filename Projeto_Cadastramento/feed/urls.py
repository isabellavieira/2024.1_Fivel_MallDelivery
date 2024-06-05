from django.urls import path
from . import views

# Definição das rotas (URLs) e mapeamento para as views correspondentes
urlpatterns = [
    path('feed_produtos/', views.feed_produtos, name='feed_produtos')
]
