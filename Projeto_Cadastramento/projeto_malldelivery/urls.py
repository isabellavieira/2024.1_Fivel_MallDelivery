from django.contrib import admin
from django.urls import path, include
from cadastramento import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name = 'inicio'),
    path('cadastramento/', include('cadastramento.urls'))
]
