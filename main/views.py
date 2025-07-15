from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def timezones_view(request):
    return render(request, 'main/timezones.html')

def login_view(request):
    return render(request, 'main/login.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Assumes you have a login view named 'login'
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})
