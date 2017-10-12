from django.conf.urls import url
from apps.cursos.views import cursos

urlpatterns = [
    url(r'^', cursos),

    
    

]