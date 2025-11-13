from django.urls import path
from . import views
urlpatterns = [
    path("", views.configuraciones, name="configuraciones"),
    path('eliminar_cuenta/', views.delete_account, name='eliminar_cuenta'),]
