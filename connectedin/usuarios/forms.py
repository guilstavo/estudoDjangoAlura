from django import forms
from django.contrib.auth.models import User

class RegistrarUsuarioForm(Forms.Form):

	nome = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	senha = forms.CharField(required=True)
	telefone = forms.CharField(required=True)
	nome_empresa = forms.CharField(required=True)

	def is_valid(self):
		valid = True
		if not super(RegistrarUsuarioForm, self).is_valid():
			self.adiciona_erro('Por Favor, verifique os dados informados.')
			valid = False

		user_existis = User.objects.filter(username=self.data['nome']).exists()
		
		if user_existis:
			self.adiciona_erro('Usuário já existente')
			valid = False

		return valid

	def adiciona_erro(self, message):
		erros = self.erros.setdefault(forms.forms.NON_FIELD_ERROS, forms.utils.ErrorList)
		error.append(message)