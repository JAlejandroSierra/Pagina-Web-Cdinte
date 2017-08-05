from django.shortcuts import render
from django.http import HttpResponse

from apps.iniciar_sesion.forms import UsuarioForm

# Create your views here.

def iniciar_sesion(request):
	return render(request, 'paginas/iniciar_sesion.html')


def usuario_view(request):
	if request.method == 'POST':
		form = UsuarioForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('iniciar_sesion')
		else:
			form = UsuarioForm()

		return render(request, 'paginas/iniciar_sesion.html', {'form':form}) 
