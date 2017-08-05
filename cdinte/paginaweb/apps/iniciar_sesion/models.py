from django.db import models

# Create your models here.


class usuario(models.Model):
	nombre = models.CharField(max_length=50)
	ApellidoPaterno=models.CharField(max_length=50)
	ApellidoMaterno = models.CharField(max_length=50)
	Correo = models.CharField(max_length=50)
	Password = models.CharField(max_length=50)
	Sexo = models.CharField(max_length=10)
	Fecha_Nacimiento = models.DateField()