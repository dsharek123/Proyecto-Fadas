
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),

    #inicio
    path('inicio/',include('inicio.urls')),

    #login
    path('',include('cuentas.urls')),

    #sign in
    path('sign/', include('cuentas.urls')),
    
    #Apps
    path('apuntes/',include('apuntes.urls')),
    path('calendario/',include('calendario.urls')),
    path('flashcard/', include('flashcard.urls')),
    path("configuraciones/", include("configuraciones.urls")),
    path("sobrenosotros/", include("sobrenosotros.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'inicio' / 'static')
