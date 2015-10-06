class UserForm(forms.ModelForm):
	"""Formulário para cadastro de aluno"""
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password')