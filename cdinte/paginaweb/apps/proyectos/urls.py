from django.conf.urls import url
from apps.proyectos.views import proyectos


urlpatterns = [
    
    url(r'^$', proyectos)
]