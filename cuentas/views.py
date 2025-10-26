from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'cuentas/home.html')
def signup(request):
    
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
                return redirect('home')
            
            except:
                return render(request, 'cuentas/signup.html',{
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
                                                
                                                
        return render(request, 'cuentas/signup.html',{
            'form':UserCreationForm,
            'error': "Las contraseñas no coinciden"
                
        })
        
        
        
        
        
def signin(request):
    if request.method == 'GET':
        return render(request, 'cuentas/signin.html', {
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'cuentas/signin.html', {
                'error': 'Username o password is incorrect'
            })
        else:
            login(request, user)
            return redirect('dashboard')    
        
        
@login_required
def signout(request):
    logout(request)
    return redirect('home')