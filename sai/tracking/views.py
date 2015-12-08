# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.utils.translation import ugettext as _

from models import Aluno, AlunoIn, AlunoOut, Pais, Instituicao
from forms import AlunoInForm, AlunoInContatoForm

# Create your views here.
def index(request):
    # template = loader.get_template('tracking/index.html')
    return render(request, 'tracking/index.html')

def map_in(request):
    return render(request, 'tracking/map-in.html')

def map_out(request):
    return render(request, 'tracking/map-out.html')

def json_map_out(request):
    # for pais in Pais.objects.all():
    return HttpResponse('Unimplemented!')


"""
Função para salvar os dados pessoais para AlunoIn
"""
@login_required
def form_in(request):
    # if this is a POST Request, process the form data
    context = None
    aluno = AlunoIn.objects.get(user=request.user)
    paises = Pais.objects.all()
    context = {'paises': paises, 'aluno':aluno}
    if request.method == 'POST':
        form = AlunoInForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Dados pessoais atualizados.')
    # request via GET method
    return render(request, 'tracking/form-in-step1.html', context)

"""
Função para salvar os dados de contato para o AlunoIn
"""
@login_required
def form_in_contato(request):
    rcontext = None
    aluno = AlunoIn.objects.get(user=request.user)
    context = {'aluno':aluno}
    if request.method == 'POST':
        form = AlunoInContatoForm(request.POST, instance=aluno)
        print form.errors
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Dados de contato atualizados.')
    # request via GET method
    return render(request, 'tracking/form-in-step2.html', context)

def form_in_instituicao(request):
    rcontext = None
    aluno = AlunoIn.objects.get(user=request.user)
    instituicoes = Instituicao.objects.all()
    context = {'aluno':aluno, 'instituicoes':instituicoes}
    if request.method == 'POST':
        instituicao = Instituicao.objects.get(pk=request.POST.get("instituicao_vinculo"))
        aluno.instituicao_vinculo = instituicao
        aluno.save
        messages.add_message(request, messages.INFO, 'Instituição de vínculo atualizada.')
    # request via GET method
    return render(request, 'tracking/form-in-step3.html', context)


def form_out(request):
    return render(request, 'tracking/form-out.html')

# User login
def user_login(request):
    # if request is a HTTP POST, try to pull out the relevant information
    if request.method == 'POST':
        # pega o username e password da view
        username = request.POST.get('username')
        password = request.POST.get('password')
        # utiliza classes do Django apra autenticar
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Sua conta está desativada")
        else:
            print "Login inválido: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'tracking/login.html', {})

