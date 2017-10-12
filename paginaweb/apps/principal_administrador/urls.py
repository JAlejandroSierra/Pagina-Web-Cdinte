from django.conf.urls import url
from apps.principal_administrador.views import index


urlpatterns = [
    
    url(r'^$',index, name='principal_index')
]