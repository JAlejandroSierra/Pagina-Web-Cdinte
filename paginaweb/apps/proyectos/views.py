from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def proyectos(request):
	return render(request, 'paginas/proyectos.html')