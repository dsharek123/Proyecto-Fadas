from django.db import models

class Tema(models.Model):
    tema = models.CharField(max_length=200)
    actividad = models.CharField(max_length=200, blank=True)
    fecha = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.tema