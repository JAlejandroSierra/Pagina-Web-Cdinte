from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
import json


# Create your views here.

class BuscarView(TemplateView):
	

	def post(self, request, *args, **kwargs):
		buscar = request.POST.get("buscalo")
		print (buscar)
		return render(request, 'informacion/buscar.html')

	
