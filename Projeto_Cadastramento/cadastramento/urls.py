from django.urls import path
from . import views

# Definição das rotas (URLs) e mapeamento para as views correspondentes
urlpatterns = [
    path('cadastrar_lojistas/', views.cadastrar_lojistas, name='cadastrar_lojistas'),
    path('login_lojistas/', views.login_lojistas, name='login_lojistas'),
    path('validar_cadastro_lojistas/', views.validar_cadastro_lojistas, name='validar_cadastro_lojistas'),
    path('validar_login_lojistas/', views.validar_login_lojistas, name='validar_login_lojistas'),

    path('intermediaria1/', views.intermediaria1, name='intermediaria1'),

    path('cadastrar_lojas/', views.cadastrar_lojas, name='cadastrar_lojas'),
    path('login_lojas/', views.login_lojas, name='login_lojas'),
    path('validar_cadastro_lojas/', views.validar_cadastro_lojas, name='validar_cadastro_lojas'),
    path('validar_login_lojas/', views.validar_login_lojas, name='validar_login_lojas'),
    
    path('cadastrar_produtos/', views.cadastrar_produtos, name='cadastrar_produtos'),
    path('validar_cadastro_produtos/', views.validar_cadastro_produtos, name='validar_cadastro_produtos')
]
