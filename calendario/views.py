from django.shortcuts import render

# Create your views here.

def vista_calendario(request):
    return render(request, 'core/calendario.html')