from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registered Successfully! Please log in.")
            return redirect('login')
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def register_portal(request):
    return render(request, 'register_portal.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def ticket(request):
    return render(request, 'ticket.html')

# Make sure you also have register_view, login_view, logout_view defined here!
