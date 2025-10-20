from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme

def _style_form_fields(form):
    for field in form.fields.values():
        existing_classes = field.widget.attrs.get('class', '')
        classes = f"{existing_classes} form-control".strip()
        field.widget.attrs['class'] = classes
    return form


def landing(request):
    return render(request, 'cuentas/landing.html')


def about(request):
    return render(request, 'cuentas/about.html')


@login_required

def home(request):
    return render(request, 'cuentas/dashboard.html')


def _get_safe_next_url(request):
    next_url = request.POST.get('next') or request.GET.get('next', '')
    if next_url and not url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return ''
    return next_url


def signin(request):
    next_url = _get_safe_next_url(request)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        _style_form_fields(form)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            redirect_to = _get_safe_next_url(request)
            if redirect_to:
                return redirect(redirect_to)
            return redirect('dashboard')
    else:
        form = AuthenticationForm(request)
        _style_form_fields(form)

    return render(request, 'cuentas/signin.html', {
        'form': form,
        'next': next_url,
    })


def signout(request):
    auth_logout(request)
    return redirect('landing')

def signup(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        _style_form_fields(form)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
        _style_form_fields(form)

    return render(request, 'cuentas/signup.html', {
        'form': form,
    })
    