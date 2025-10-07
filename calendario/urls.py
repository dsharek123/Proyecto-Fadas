from django.urls import path
from .views import vista_calendario

urlpatterns = [
    path('', vista_calendario, name='vista_calendario'),
]
