from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import  logout

@login_required
def configuraciones(request):
    return render(request,"configuraciones.html")

@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, "Tu cuenta ha sido elimada.")
        return redirect("home")
    return render(request,"eliminar_cuenta.html")
