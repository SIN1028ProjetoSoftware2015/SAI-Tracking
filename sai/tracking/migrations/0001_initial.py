# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField(null=True)),
                ('matricula', models.CharField(max_length=20, null=True, blank=True)),
                ('endereco', models.CharField(max_length=200, null=True, blank=True)),
                ('cidade', models.CharField(max_length=100, null=True, blank=True)),
                ('estado', models.CharField(max_length=5, null=True, blank=True)),
                ('telefone', models.CharField(max_length=20, null=True, blank=True)),
                ('email', models.CharField(max_length=200, null=True, blank=True)),
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
            name='Intercambio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cidade', models.CharField(max_length=200)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('modalidade', models.IntegerField(choices=[(1, b'Gradua\xc3\xa7\xc3\xa3o'), (2, b'Especializa\xc3\xa7\xc3\xa3o'), (3, b'Mestrado'), (4, b'Doutorado'), (5, b'P\xc3\xb3s-Doutorado'), (6, b'Est\xc3\xa1gio')])),
            ],
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
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AlunoIn',
            fields=[
                ('aluno_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tracking.Aluno')),
                ('nome_pai', models.CharField(max_length=200, null=True, blank=True)),
                ('nome_mae', models.CharField(max_length=200, null=True, blank=True)),
                ('local_nascimento', models.CharField(max_length=150, null=True, blank=True)),
                ('cont_nome', models.CharField(max_length=200, null=True, blank=True)),
                ('cont_parentesco', models.CharField(max_length=50, null=True, blank=True)),
                ('cont_endereco', models.CharField(max_length=200, null=True, blank=True)),
                ('cont_telefone', models.CharField(max_length=20, null=True, blank=True)),
                ('cont_email', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Aluno estrangeiro',
                'verbose_name_plural': 'Alunos estrangeiros',
            },
            bases=('tracking.aluno',),
        ),
        migrations.CreateModel(
            name='AlunoOut',
            fields=[
                ('aluno_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tracking.Aluno')),
                ('contato_emerg', models.CharField(max_length=200, null=True, blank=True)),
                ('curso_ufsm', models.CharField(max_length=70, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Aluno brasileiro',
                'verbose_name_plural': 'Alunos brasileiros',
            },
            bases=('tracking.aluno',),
        ),
        migrations.AddField(
            model_name='intercambio',
            name='aluno',
            field=models.ForeignKey(to='tracking.Aluno'),
        ),
        migrations.AddField(
            model_name='intercambio',
            name='pais',
            field=models.ForeignKey(to='tracking.Pais'),
        ),
        migrations.AddField(
            model_name='intercambio',
            name='programa',
            field=models.ForeignKey(to='tracking.Programa'),
        ),
        migrations.AddField(
            model_name='intercambio',
            name='universidade_destino',
            field=models.ForeignKey(to='tracking.Instituicao'),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='pais',
            field=models.ForeignKey(to='tracking.Pais'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='pais',
            field=models.ForeignKey(blank=True, to='tracking.Pais', null=True),
        ),
        migrations.AddField(
            model_name='aluno',
            name='user',
            field=models.OneToOneField(editable=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='alunoin',
            name='instituicao_vinculo',
            field=models.ForeignKey(blank=True, to='tracking.Instituicao', null=True),
        ),
    ]
