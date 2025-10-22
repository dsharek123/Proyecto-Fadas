from django.shortcuts import render
from django.contrib.auth.decorators import login_required 

# Create your views here.

@login_required
def vista_calendario(request):
    return render(request, 'core/calendario.html')