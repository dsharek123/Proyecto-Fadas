from django.urls import path
from .views import vista_calendario

app_name = 'calendario'

urlpatterns = [
    path('', vista_calendario, name='index'),
]
