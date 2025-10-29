from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_apunte, name='crear_apunte'),
    path('seleccion/', views.seleccion_apuntes, name='seleccion_apuntes'),
]