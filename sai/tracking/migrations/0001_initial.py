# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField()),
                ('matricula', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=5)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('endereco', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=50)),
                ('contato', models.CharField(max_length=100)),
                ('contato_cargo', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Institui\xe7\xe3o',
                'verbose_name_plural': 'Institui\xe7\xf5es',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'verbose_name': 'Pa\xeds',
                'verbose_name_plural': 'Pa\xedses',
            },
        ),
        migrations.AddField(
            model_name='instituicao',
            name='pais',
            field=models.ForeignKey(to='tracking.Pais'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='pais',
            field=models.ForeignKey(to='tracking.Pais'),
        ),
    ]
