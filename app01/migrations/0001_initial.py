# Generated by Django 4.2.3 on 2023-07-27 22:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome do presente')),
                ('detalhes', models.TextField(default='texto aqui', max_length=500, verbose_name='Descricao do presente')),
                ('quantidade_desejada', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)], verbose_name='Quantidade desejada')),
                ('quantidade_recebida', models.PositiveIntegerField()),
                ('quantidade_restante', models.PositiveIntegerField()),
                ('imagem', models.ImageField(upload_to='presentes/', verbose_name='Imagem do Presente')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaPresente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_presenteada', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)], verbose_name='Quantidade')),
                ('nome_pessoa', models.CharField(max_length=200, verbose_name='Nome de quem vai dar o presente')),
                ('nome_presente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.presente')),
            ],
            options={
                'verbose_name': 'Pessoa Presente',
                'verbose_name_plural': 'Pessoas Presente',
            },
        ),
    ]
