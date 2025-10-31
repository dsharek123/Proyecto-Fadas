from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApunteForm
from .models import Apunte
from django.contrib.auth.decorators import login_required

def crear_apunte(request):
    if request.method == 'POST':
        form = ApunteForm(request.POST)
        if form.is_valid():
            apunte = form.save(commit=False)
            apunte.usuario = request.user
            apunte.save()
            return redirect('apuntes_creados')
    else:
        form = ApunteForm()
    return render(request, 'apuntes/crear_apunte.html', {'form':form})

def seleccion_apuntes(request):
    return render(request, 'apuntes/seleccion_apuntes.html')

def apuntes_creados(request):
    apuntes = Apunte.objects.filter(usuario=request.user).order_by('-creado')
    return render(request, 'apuntes/apuntes_creados.html',{'apuntes':apuntes})

def eliminar_apunte(request, apunte_id):
    apunte = get_object_or_404(Apunte, id=apunte_id, usuario=request.user)
    if request.method == 'POST':
        apunte.delete()
        return redirect('apuntes_creados')
    return render(request, 'apuntes/apuntes_creados.html')

def detalle_apunte(request, apunte_id):
    apunte = get_object_or_404(Apunte, id=apunte_id, usuario=request.user)
    return render(request, 'apuntes/detalle_apunte.html', {'apunte':apunte})