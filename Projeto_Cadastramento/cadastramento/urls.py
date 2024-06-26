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
    
    path('cadastrar_produtos/<int:loja_id>/', views.cadastrar_produtos, name='cadastrar_produtos'),
    path('validar_cadastro_produtos/<int:loja_id>/', views.validar_cadastro_produtos, name='validar_cadastro_produtos'),

    path('feed/<int:loja_id>/', views.aprovacao, name='aprovacao'),
    path('loja_em_analise/', views.loja_em_analise, name='loja_em_analise'),
    path('verificar_status_loja/<int:loja_id>/', views.verificar_status_loja, name='verificar_status_loja'),


]


