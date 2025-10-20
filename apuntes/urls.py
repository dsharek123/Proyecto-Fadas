from django.urls import path
from . import views

app_name = 'apuntes'

urlpatterns = [
    path('crear/', views.crear_apunte, name='Crear Apunte'),
]