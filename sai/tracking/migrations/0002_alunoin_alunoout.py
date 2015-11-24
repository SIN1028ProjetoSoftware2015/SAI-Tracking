# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlunoIn',
            fields=[
                ('aluno_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tracking.Aluno')),
                ('nome_pai', models.CharField(max_length=200)),
                ('nome_mae', models.CharField(max_length=200)),
                ('local_nascimento', models.CharField(max_length=150)),
                ('cont_nome', models.CharField(max_length=200)),
                ('cont_parentesco', models.CharField(max_length=50)),
                ('cont_endereco', models.CharField(max_length=200)),
                ('cont_telefone', models.CharField(max_length=20)),
                ('cont_email', models.CharField(max_length=200)),
                ('instituicao_vinculo', models.ForeignKey(to='tracking.Instituicao')),
            ],
            bases=('tracking.aluno',),
        ),
        migrations.CreateModel(
            name='AlunoOut',
            fields=[
                ('aluno_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tracking.Aluno')),
                ('contato_emerg', models.CharField(max_length=200)),
                ('curso_ufsm', models.CharField(max_length=70)),
            ],
            bases=('tracking.aluno',),
        ),
    ]
