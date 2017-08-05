from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def producto(request):
	return render(request, 'paginas/productos_servicios.html')

# Create your views here.
