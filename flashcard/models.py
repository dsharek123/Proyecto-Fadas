from django.db import models
from django.contrib.auth.models import User

class Flashcard(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pregunta = models.TextField()
    respuesta = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Flashcard de {self.usuario.username}: {self.pregunta[:50]}..."