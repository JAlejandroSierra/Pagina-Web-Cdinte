from django.conf.urls import url
from apps.contacto.views import contacto


urlpatterns = [
    
    url(r'^$', contacto)
]