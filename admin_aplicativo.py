from django.contrib import admin
from .models import Presente

# Register your models here.
class PresenteAdmin(admin.ModelAdmin):
    list_display = ['nome','quantidade']
    search_fields = ['nome']

admin.site.register(Presente, PresenteAdmin)

