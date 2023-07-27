from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.messages import constants
from django.db import DatabaseError
from .models import Presente
from .forms import MF_CadastrarPresente

# Create your views here.
def home(request):
    presentes = Presente.objects.all()
    return render(request, 'index.html', {'presentes':presentes})

def page_not_found(request, slug):
    return render(request, '404.html', status=404)


def presentear(request):
    form = MF_CadastrarPresente()
    return render(request, 'presentear.html', {'form':form})



def valida_cadastro_presente(request):
    if request.method == 'POST':
        form = MF_CadastrarPresente(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request, 'presentear.html', {'form': MF_CadastrarPresente(), 'sucesso':True})
            except DatabaseError as erro:
                return render(request, 'limite.html')
    else:
        form = MF_CadastrarPresente()

    return render(request, 'presentear.html', {'form': form})

