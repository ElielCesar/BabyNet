from django.contrib import admin
from .models import Presente, PessoaPresente

# Register your models here.
class PresenteAdmin(admin.ModelAdmin):
    list_display = ['nome','quantidade']
    search_fields = ['nome']

admin.site.register(Presente, PresenteAdmin)

class PessoaPresenteAdmin(admin.ModelAdmin):
    list_display = ['nome_pessoa', 'nome_presente', 'quantidade_presenteada']
    ordering = ['nome_presente']
    search_fields = ['nome_pessoa'] # não pode ser presente por causa da chave estrangeira

admin.site.register(PessoaPresente, PessoaPresenteAdmin)
