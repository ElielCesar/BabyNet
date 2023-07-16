from django.shortcuts import render
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




