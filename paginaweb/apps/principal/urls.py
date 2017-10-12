from django.conf.urls import url
from apps.principal.views import principal


urlpatterns = [
    
    url(r'^$',principal, name='principal')
]