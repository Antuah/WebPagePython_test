from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth.decorators import login_required
import json
from .message import message as Message

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión después del registro
            return redirect('home')  # Redirigir a la página principal
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    message = {
        "type": "info",
        "message": "Se ha cerrado sesión exitosamente",
        "code": 200,
        "img": "https://png.pngtree.com/png-vector/20220520/ourmid/pngtree-happy-emoji-emoticon-showing-double-thumbs-up-like-png-image_4708251.png"
    }
    return render(request, "login.html", {"message": message})