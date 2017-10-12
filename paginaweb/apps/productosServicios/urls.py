from django.conf.urls import url
from apps.productosServicios.views import producto

urlpatterns = [
    url(r'^', producto),
]