from django.contrib import admin
from django.urls import path, include
from cadastramento import views
from django.conf import settings
from django.conf.urls.static import static

# Definição das rotas (URLs) e mapeamento para as views correspondentes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name = 'inicio'),
    path('cadastramento/', include('cadastramento.urls')),
    path('feed/', include('feed.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)