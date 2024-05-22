from django.contrib import admin
from django.urls import path, include
from cadastramento import views

# Definição das rotas (URLs) e mapeamento para as views correspondentes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name = 'inicio'),
    path('cadastramento/', include('cadastramento.urls'))
]
