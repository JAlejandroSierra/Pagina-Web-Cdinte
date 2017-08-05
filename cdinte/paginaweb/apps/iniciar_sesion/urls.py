from django.conf.urls import url
from apps.iniciar_sesion.views import iniciar_sesion, usuario_view


urlpatterns = [
    
    url(r'^$', iniciar_sesion, name='iniciar_sesion'),
    url(r'^nuevo$', usuario_view, name='usuario_view'),
]