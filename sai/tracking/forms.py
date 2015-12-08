from django import forms
from models import Aluno, AlunoIn

class AlunoForm(forms.ModelForm):

	class Meta:
		model = Aluno
		fields = ('nome', 'data_nascimento', 'matricula',
			'endereco', 'cidade', 'estado', 'pais',
			'telefone', 'email')


class AlunoInForm(forms.ModelForm):
    class Meta:
        model = AlunoIn
        fields = ('nome', 'data_nascimento', 'matricula',
            'endereco', 'cidade', 'estado', 'pais',
            'telefone', 'email', 'passaporte', 'nome_pai',
            'nome_mae', 'local_nascimento')

class AlunoInContatoForm(forms.ModelForm):
    class Meta:
        model = AlunoIn
        fields = ('cont_nome', 'cont_parentesco',
            'cont_endereco', 'cont_telefone',
            'cont_email', 'instituicao_vinculo')
