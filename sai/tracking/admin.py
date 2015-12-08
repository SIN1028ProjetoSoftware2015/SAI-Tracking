from django.contrib import admin
from .models import Pais, Instituicao, AlunoIn, AlunoOut, Programa, Intercambio

#from models import UserProfile

# classes for customization
class IntercambioAdmin(admin.ModelAdmin):
	list_display = ('get_aluno', 'get_programa', 'get_universidade_destino');

admin.site.register(Pais)
admin.site.register(Instituicao)
admin.site.register(AlunoIn)
admin.site.register(AlunoOut)
admin.site.register(Programa)
admin.site.register(Intercambio, IntercambioAdmin)
