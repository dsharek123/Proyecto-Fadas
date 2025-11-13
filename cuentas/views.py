from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib import messages

def home(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    return render(request, 'cuentas/home.html')

@never_cache 

def signup(request):

    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == "GET":
            return render(request, 'cuentas/signup.html', {
                'form': UserCreationForm
            })
        else:
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if password1 != password2:
                return render(request, 'cuentas/signup.html', {
                    'form': UserCreationForm,
                    'error': "Las contraseñas no coinciden"
                })

            try:
                validate_password(password1)  
            except ValidationError as e:

                return render(request, 'cuentas/signup.html', {
                    'form': UserCreationForm,
                    'error': e.messages  
                })

            try:
                user = User.objects.create_user(
                    username=username,
                    password=password1
                )
                user.save()

                login(request, user)
                return redirect('inicio')

            except Exception:
                return render(request, 'cuentas/signup.html', {
                    'form': UserCreationForm,
                    'error': "El usuario ya existe o no se pudo crear la cuenta"
                })
        
        
        
        
@never_cache 
def signin(request):
    if request.user.is_authenticated:
            return redirect('inicio')
    else:
        if request.method == 'GET':
            return render(request, 'cuentas/signin.html', {
            })
        else:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            
            if user is None:
                return render(request, 'cuentas/signin.html', {
                    'error': 'Usuario o Contraseña son incorrectos'
                })
            else:
                login(request, user)
                return redirect('inicio')    
        
        
@login_required
def signout(request):
    logout(request)
    return redirect('home')

