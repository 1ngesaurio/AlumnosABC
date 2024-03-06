from django.db import models

class Alumno(models.Model):
    carnet = models.CharField(max_length=14, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correoElectronico = models.EmailField(unique=True)
    fechaNacimiento = models.DateField()

    def __str__(self):
        return self.carnet
