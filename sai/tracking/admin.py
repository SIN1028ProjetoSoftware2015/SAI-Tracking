from django.contrib import admin
from .models import Pais, Instituicao, AlunoIn, AlunoOut

#from models import UserProfile

admin.site.register(Pais)
admin.site.register(Instituicao)
admin.site.register(AlunoIn)
admin.site.register(AlunoOut)
