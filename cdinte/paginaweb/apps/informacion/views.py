from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.

class BuscarView(TemplateView):


	def post(self, request, *args, **kwargs):

		buscar = request.POST['buscalo']
		if buscar== "cdinte" or buscar=="CDINTE" or buscar=="Cdinte" or buscar=="informes":
					
				return render(request, 'paginas/quienes_somos.html')

		

		if buscar=="administrador"or buscar=="ADMINISTRADOR" or buscar=="Administrador":
				
				return render(request, 'paginas/boton_administrador.html')

		if buscar=="Principal" or buscar=="PRINCIPAL" or buscar=="principal" or buscar=="inicio":

				return render(request, 'paginas/principal.html')



		else:

				return render(request, 'paginas/error.html')


	