from django.db import models
from django.contrib.auth.models import User

class Tema(models.Model):
    
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    tema = models.CharField(max_length=200)
    actividad = models.CharField(max_length=200, blank=True)
    fecha = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.tema