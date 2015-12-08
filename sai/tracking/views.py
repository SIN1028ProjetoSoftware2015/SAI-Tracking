# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from models import Aluno, Pais
from forms import AlunoForm

# Create your views here.
def index(request):
    # template = loader.get_template('tracking/index.html')
    return render(request, 'tracking/index.html')

def map_in(request):
    return render(request, 'tracking/map-in.html')

def map_out(request):
    return render(request, 'tracking/map-out.html')

@login_required
def form_in(request):
    # if this is a POST Request, process the form data
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            return HttpResponse(u"Form válido")
        else:
            return HttpResponse(u"Form inválido")
    # if this is a GET requeest show de form with data
    else:
        u = User.objects.get(username=request.user.username)
        data_aluno = u.aluno
        paises = Pais.objects.all()
        print paises
        # if a GET request, show the form
        return render(request, 'tracking/form-in-step1.html', {'aluno': data_aluno, 'paises':paises})

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

