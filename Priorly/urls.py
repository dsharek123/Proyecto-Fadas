
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),

    #home
    path('home/',include('home.urls')),

    #login
    path('',include('cuentas.urls')),

    #sign in
    path('sign/', include('cuentas.urls')),
    
    #Apps
    path('apuntes/',include('apuntes.urls')),
    path('calendario/',include('calendario.urls')),
    path('flashcard/', include('flashcard.urls')),
]
