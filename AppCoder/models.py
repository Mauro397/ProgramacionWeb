from msilib.schema import Class
from django.db import models

# Create your models here.

class Gimnasio(models.Model):

    def __str__(self):

        return f"Nombre: {self.nombre} ------- FechaDeCreacion: {self.fechaCreacion} ------- Localizacion: {self.localicacion}" 

    nombre=models.CharField(max_length=60)
    fechaCreacion=models.DateField()
    localicacion=models.CharField(max_length=30)

class Maquinas(models.Model):

    def __str__(self):

        return f"Nombre: {self.nombre} ------- FechaDeCreacion: {self.zonaDeTrabajo} ------- Localizacion: {self.pesoMax}"       
    
    nombre=models.CharField(max_length=30)
    zonaDeTrabajo=models.CharField(max_length=60)
    pesoMax=models.IntegerField()

class Entrenadores(models.Model):

    def __str__(self):

        return f"Nombre: {self.nombre} ------- FechaDeCreacion: {self.apellido} ------- Localizacion: {self.especialidad}"
        
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=60)
    especialidad=models.CharField(max_length=60)


    

