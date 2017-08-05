from django import forms
from apps.iniciar_sesion.models import usuario



class UsuarioForm(forms.ModelForm):

	class Meta:

		model= usuario


		fields = [

			'nombre',
			'ApellidoPaterno',
			'ApellidoMaterno',
			'Correo',
			'Password',
			'Sexo',
			'Fecha_Nacimiento',
		]
		labels = {

			'nombre': 'Nombre',
			'ApellidoPaterno': 'Apellido Paterno',
			'ApellidoMaterno': 'Apellido Materno',
			'Correo': 'Correo',
			'Password': 'Password',
			'Sexo': 'Sexo',
			'Fecha_Nacimiento': 'Feha de Nacimiento',
		}
		widgets = {

			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'ApellidoPaterno': forms.TextInput(attrs={'class':'form-control'}),
			'ApellidoMaterno': forms.TextInput(attrs={'class':'form-control'}),
			'Correo': forms.TextInput(attrs={'class':'form-control'}),
			'Password': forms.TextInput(attrs={'class':'form-control'}),
			'Sexo': forms.TextInput(attrs={'class':'form-control'}),
			'Fecha_Nacimiento': forms.TextInput(attrs={'class':'form-control'}),
		}
