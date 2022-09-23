from msilib.schema import Class
from django.db import models

# Create your models here.

class Gimnasio(models.Model):

    nombre=models.CharField(max_length=60)
    fechaCreacion=models.DateField()
    Localicacion=models.CharField(max_length=30)

class Maquinas(models.Model):

    nombre=models.CharField(max_length=30)
    zonaDeTrabajo=models.CharField(max_length=60)
    pesoMax=models.IntegerField()

class Entrenadores(models.Model):

    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=60)
    especialidad=models.CharField(max_length=60)


    

