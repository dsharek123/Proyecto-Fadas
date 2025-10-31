from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/cuentas/signin/')
def home_view(request):
    return render(request, "inicio.html")