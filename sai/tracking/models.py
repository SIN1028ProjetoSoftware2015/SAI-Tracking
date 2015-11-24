# -*- coding: utf-8 -*-
from django.db import models
from django import forms
from django.contrib.auth.models import User

class Pais(models.Model):
    """This model represent all countries registered in APP"""
    nome = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name='País'
        verbose_name_plural='Países'

class Instituicao(models.Model):
    """ This class is used to store information about Universities """
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais)
    telefone = models.CharField(max_length=50)
    contato = models.CharField(max_length=100)
    contato_cargo = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name='Instituição'
        verbose_name_plural = 'Instituições'


class Aluno(models.Model):
    """ This class is used to store information about students """
    nome = models.CharField(max_length=200);
    # sobrenome = models.CharField(max_length=200)
    # profile_image = models.ImageField(upload_to='profile_images', blank=True)
    data_nascimento = models.DateField()
    matricula = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    # numero = models.CharField(max_length=10)
    # complemento = models.CharField(max_length=50)
    # bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=5)
    pais = models.ForeignKey(Pais)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class AlunoIn(Aluno):
    """
    Description: Model Description
    """
    nome_pai = models.CharField(max_length=200)
    nome_mae = models.CharField(max_length=200)
    local_nascimento = models.CharField(max_length=150)
    cont_nome = models.CharField(max_length=200)
    cont_parentesco = models.CharField(max_length=50)
    cont_endereco = models.CharField(max_length=200)
    cont_telefone = models.CharField(max_length=20)
    cont_email = models.CharField(max_length=200)
    instituicao_vinculo = models.ForeignKey(Instituicao)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name='Aluno estrangeiro'
        verbose_name_plural = 'Alunos estrangeiros'



class AlunoOut(Aluno):
    """
    Description: Model Description
    """
    contato_emerg = models.CharField(max_length=200)
    curso_ufsm = models.CharField(max_length=70)

    class Meta:
        verbose_name='Aluno brasileiro'
        verbose_name_plural = 'Alunos brasileiros'


            