from django import forms
from .models import Presente, PessoaPresente

class MF_CadastrarPresente(forms.ModelForm):
    class Meta:
        model = PessoaPresente
        fields = ['nome_presente', 'quantidade_presenteada', 'nome_pessoa']

        widgets = {
        'nome_presente': forms.Select(attrs={'class':'form-control mt-2'}),
        'quantidade_presenteada': forms.NumberInput(attrs={'class':'form-control mt-2'}),
        'nome_pessoa': forms.TextInput(attrs={'class':'form-control mt-2'}),
        }












