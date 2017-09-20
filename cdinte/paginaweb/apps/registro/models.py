from django.db import models

from __future__ import unicode_literals

class Usuarios(models.Model):
	nombre = models.CharField(max_length=30)
	correos = models.CharField(max_length=40)
	opiniones = models.DateTimeField(max_length=500)
	fecha = models.DateTimeField(max_length=10)

class User(models.Model):
	nombre = models.CharField(max_length=30)
	correos = models.CharField(max_length=40)
	opiniones = models.CharField(max_length=500)
	fecha = models.CharField(max_length=10)

