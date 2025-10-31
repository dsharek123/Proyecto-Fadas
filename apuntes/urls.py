from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_apunte, name='crear_apunte'),
    path('seleccion/', views.seleccion_apuntes, name='seleccion_apuntes'),
    path('creados/',views.apuntes_creados, name='apuntes_creados'),
    path('eliminar/<int:apunte_id>/', views.eliminar_apunte, name='eliminar_apunte'),
    path('detalle/<int:apunte_id>/', views.detalle_apunte, name='detalle_apunte'),
]