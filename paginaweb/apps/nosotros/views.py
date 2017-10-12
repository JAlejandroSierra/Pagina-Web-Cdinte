from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def quienes_somos(request):
	return render(request, 'paginas/quienes_somos.html')