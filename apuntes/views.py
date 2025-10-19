from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApunteForm
from .models import Apunte
from django.contrib.auth.decorators import login_required

@login_required
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
