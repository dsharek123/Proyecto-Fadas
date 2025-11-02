from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

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
            if request.POST['password1'] ==request.POST['password2']:
                try:
                    user = User.objects.create_user(username = request.POST['username'],
                    password = request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('inicio')
                
                except:
                    return render(request, 'cuentas/signup.html',{
                        'form': UserCreationForm,
                        'error': 'El usuario ya existe'
                    })
                                                    
                                                    
            return render(request, 'cuentas/signup.html',{
                'form':UserCreationForm,
                'error': "Las contraseñas no coinciden"
                    
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