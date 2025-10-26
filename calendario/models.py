from django.db import models

# Create your models here.
class Tema(models.Model):
    tema = models.CharField(max_length=200)
    actividad = models.CharField(max_length=200, blank=True)
    fecha = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.tema