from django.conf.urls import url
from apps.quienes_somos.views import quienes_somos


urlpatterns = [
    
    url(r'^$', quienes_somos)
]
