from django.contrib import admin
from .models import Lojistas, Lojas, Produtos

@admin.register(Lojas)
class LojasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'tel', 'status')
    list_filter = ('status',)
    actions = ['aprovar_lojas', 'rejeitar_lojas']

    def aprovar_lojas(self, request, queryset):
        queryset.update(status='approved')
        self.message_user(request, "Lojas aprovadas com sucesso.")
    aprovar_lojas.short_description = 'Aprovar lojas selecionadas'

    def rejeitar_lojas(self, request, queryset):
        queryset.update(status='rejected')
        self.message_user(request, "Lojas rejeitadas com sucesso.")
    rejeitar_lojas.short_description = 'Rejeitar lojas selecionadas'

admin.site.register(Lojistas)
admin.site.register(Produtos)


