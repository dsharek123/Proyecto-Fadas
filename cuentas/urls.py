from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('sobre-nosotros/', views.about, name='about'),
    path('dashboard/', views.home, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
]