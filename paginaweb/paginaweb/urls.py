"""paginaweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^principal/', include ('apps.principal.urls', namespace="principal")),
    url(r'^principal_administrador/', include ('apps.principal_administrador.urls', namespace="principal_administrador")),
    url(r'^quienes_somos/', include ('apps.quienes_somos.urls', namespace="quienes_somos")),
    url(r'^nosotros/', include ('apps.quienes_somos.urls', namespace="quienes_somos")),
    url(r'^productos_servicios/', include ('apps.productosServicios.urls', namespace="productos_servicios")),
    url(r'^cursos/', include ('apps.cursos.urls', namespace="cursos")),
    url(r'^contacto/', include ('apps.contacto.urls', namespace="contacto")),
    url(r'^proyectos/', include ('apps.proyectos.urls', namespace="proyectos")),
    url(r'^usuario/', include('apps.usuario.urls', namespace='usuario')),
    url(r'^informacion/',include('apps.informacion.urls', namespace='informacion')),
     url(r'^logout/', logout_then_login, name='logout'),
     url(r'^accounts/login/', login, {'template_name':'iniciar_sesion.html'}, name='login'),
    url(r'^$',login, {'template_name':'iniciar_sesion.html'}, name='login'),
    
]
