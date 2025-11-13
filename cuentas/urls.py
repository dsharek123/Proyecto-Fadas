from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.signup, name='crear_usuario'),
    path('signin/', views.signin, name = 'identificacion' ),
    path('signout/', views.signout, name = "cerrar_sesion"),
]