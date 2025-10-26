from django.urls import path
from .views import vista_calendario, nuevo_tema, editar_tema, eliminar_tema

urlpatterns = [
    path('', vista_calendario, name='vista_calendario'),
    path('nuevo_tema/', nuevo_tema, name='nuevo_tema'),
    path('editar_tema/<int:tema_id>/', editar_tema, name='editar_tema'),
    path('eliminar_tema/<int:tema_id>/', eliminar_tema, name='eliminar_tema'),
]
