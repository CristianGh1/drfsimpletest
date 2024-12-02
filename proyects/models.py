from django.db import models

class Proyect(models.Model):
    nombre_proyecto = models.CharField(max_length=200)
    rut = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
