from django.conf import settings                
from django.conf.urls.static import static      
from django.urls import path, include
from . import views

urlpatterns = [
    # joga diretamente para a home
    path('', views.home, name='home'),
    path('presentear/<int:id>/', views.presentear, name='presentear'),
    path('valida_cadastro_presente/', views.valida_cadastro_presente, name='valida_cadastro_presente'),
    # qualquer outra url jogue para 404
    path('<path:slug>/', views.page_not_found),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
