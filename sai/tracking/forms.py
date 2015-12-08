from django import forms
from models import Aluno

class AlunoForm(forms.ModelForm):
	
	class Meta:
		model = Aluno
		fields = ('nome', 'data_nascimento', 'matricula', 
			'endereco', 'cidade', 'estado', 'pais', 
			'telefone', 'email')