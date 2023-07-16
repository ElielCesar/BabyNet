from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Presente(models.Model):
    nome = models.CharField(verbose_name='Nome do presente', max_length=200)
    detalhes = models.TextField(verbose_name='Descricao do presente', max_length=500, default='texto aqui')
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade desejada',
          validators = [ MaxValueValidator(50),
                         MinValueValidator(1) ] )
    imagem = models.ImageField(upload_to='presentes/', verbose_name='Imagem do Presente')

    def __str__(self):
        return self.nome





