from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe

# Create your models here.
class Presente(models.Model):
    nome = models.CharField(verbose_name='Nome do presente', max_length=200)
    detalhes = models.TextField(verbose_name='Descricao do presente', max_length=500, default='texto aqui')
    quantidade_desejada = models.PositiveIntegerField(verbose_name='Quantidade desejada', default=1,
          validators = [ MaxValueValidator(50), MinValueValidator(1) ] )
    quantidade_recebida = models.PositiveIntegerField()
    quantidade_restante = models.PositiveIntegerField()
    imagem = models.ImageField(upload_to='presentes/', verbose_name='Imagem do Presente')

    def __str__(self):
        return self.nome
    
    @mark_safe
    def img_presente(self):
        return f"<img width='60px' src='{self.imagem.url}'>"


class PessoaPresente(models.Model):
    nome_presente = models.ForeignKey(Presente, on_delete=models.CASCADE)
    quantidade_presenteada = models.PositiveIntegerField(verbose_name='Quantidade',
          validators = [ MaxValueValidator(50),
                         MinValueValidator(1) ] )
    nome_pessoa = models.CharField(verbose_name='Nome de quem vai dar o presente', max_length=200)

    def __str__(self):
        return f'{self.nome_pessoa} : {self.nome_presente}'
    
    class Meta:
        verbose_name = 'Pessoa Presente'
        verbose_name_plural = 'Pessoas Presente'

    @property
    def qtd_desejada(self):
        return self.nome_presente.quantidade_desejada # vou usar isso para fazer a conta
    
    @property
    def qtd_restante(self):
        return self.nome_presente.quantidade_restante # vou usar isso para fazer a conta
    
@receiver(pre_save, sender=PessoaPresente)
def antes_de_salvar_presente(sender, instance, **kwargs):
    quantidade_desejada = instance.qtd_desejada # não pode alterar

    quantidade_presenteada = instance.quantidade_presenteada # vai sempre alterar
    quantidade_recebida = instance.nome_presente.quantidade_recebida # vai sempre alterar

    # salvar no model Presente
    instance.nome_presente.quantidade_recebida = quantidade_recebida + quantidade_presenteada
    quantidade_recebida = instance.nome_presente.quantidade_recebida
    quantidade_restante_signal = quantidade_desejada - quantidade_recebida
    instance.nome_presente.quantidade_restante = quantidade_restante_signal
    instance.nome_presente.save()

