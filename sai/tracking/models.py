# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Pais(models.Model):
    """This model represent all countries registered in APP"""
    nome = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.nome

    def get_alunos_modalidade(self, modalidade=None):
        if modalidade is not None:
            return Intercambio.objects.filter(modalidade=modalidade, pais=self).count()
        else:
            return None

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
    user = models.OneToOneField(User, unique=True, editable=False)
    nome = models.CharField(max_length=200);
    # sobrenome = models.CharField(max_length=200)
    # profile_image = models.ImageField(upload_to='profile_images', blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    matricula = models.CharField(max_length=20, null = True, blank=True)
    endereco = models.CharField(max_length=200, null = True, blank=True)
    # numero = models.CharField(max_length=10)
    # complemento = models.CharField(max_length=50)
    # bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100, null = True, blank=True)
    estado = models.CharField(max_length=5, null = True, blank=True)
    pais = models.ForeignKey(Pais, null=True, blank=True)
    telefone = models.CharField(max_length=20, null = True, blank=True)
    email = models.CharField(max_length=200)
    passaporte = models.CharField(max_length=20, null=True, blank=True)

    #Overriding
    def save(self, *args, **kwargs):
        #check if the row with this hash already exists.
        if not self.pk:
            parts = self.nome.lower().split(" ")
            f_name = parts[0]
            l_name  = parts[-1]
            username =  f_name + '_' + l_name
            userpass = User.objects.make_random_password()
            new_user = User.objects.create_user(username, self.email, userpass,
                first_name=f_name, last_name=l_name)
            self.user = new_user
        super(Aluno, self).save(*args, **kwargs)


    def __unicode__(self):
        return self.nome


class AlunoIn(Aluno):
    """
    Description: Model Description
    """
    nome_pai = models.CharField(max_length=200, null = True, blank=True)
    nome_mae = models.CharField(max_length=200, null = True, blank=True)
    local_nascimento = models.CharField(max_length=150, null = True, blank=True)
    cont_nome = models.CharField(max_length=200, null = True, blank=True)
    cont_parentesco = models.CharField(max_length=50, null = True, blank=True)
    cont_endereco = models.CharField(max_length=200, null = True, blank=True)
    cont_telefone = models.CharField(max_length=20, null = True, blank=True)
    cont_email = models.CharField(max_length=200, null = True, blank=True)
    instituicao_vinculo = models.ForeignKey(Instituicao, null = True, blank=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name='Aluno estrangeiro'
        verbose_name_plural = 'Alunos estrangeiros'


class AlunoOut(Aluno):
    """
    Description: Model Description
    """
    contato_emerg = models.CharField(max_length=200, null = True, blank=True)
    curso_ufsm = models.CharField(max_length=70, null = True, blank=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name='Aluno brasileiro'
        verbose_name_plural = 'Alunos brasileiros'


class Programa(models.Model):
    """
    Description: Model Description
    """
    descricao = models.CharField(max_length=200)

    def __unicode__(self):
        return self.descricao


class Intercambio(models.Model):
    """
    Description: Intercambio
    """
    GRADUACAO = 1
    ESPECIALIZACAO = 2
    MESTRADO = 3
    DOUTORADO = 4
    POS_DOUTORADO = 5
    ESTAGIO = 6
    MODALIDADE_CHOICES = (
        (GRADUACAO, "Graduação"),
        (ESPECIALIZACAO, "Especialização"),
        (MESTRADO, "Mestrado"),
        (DOUTORADO, "Doutorado"),
        (POS_DOUTORADO, "Pós-Doutorado"),
        (ESTAGIO, "Estágio"),
    )
    aluno = models.ForeignKey(Aluno)
    universidade_destino = models.ForeignKey(Instituicao)
    programa = models.ForeignKey(Programa)
    cidade = models.CharField(max_length=200)
    pais = models.ForeignKey(Pais)
    data_inicio = models.DateField(auto_now=False, auto_now_add=False)
    data_fim = models.DateField(auto_now=False, auto_now_add=False)
    modalidade = models.IntegerField(choices=MODALIDADE_CHOICES)

    def get_aluno(self):
        return self.aluno.nome

    def get_programa(self):
        return self.programa.descricao

    def get_universidade_destino(self):
        return self.universidade_destino.nome

    get_aluno.short_description = 'Aluno'
    get_programa.short_description = 'Programa'
    get_universidade_destino.short_description = 'Universidade'

    def __unicode__(self):
        return ''.join([self.get_aluno(),
            ' | ', self.get_programa(),
            ' | ', self.get_universidade_destino()])