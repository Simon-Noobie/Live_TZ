from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def timezones_view(request):
    user_profile = request.user.userprofile
    all_timezones = [
        ('UTC', 'UTC'),
        ('America/New_York', 'New York'),
        ('Europe/London', 'London'),
        ('Asia/Kolkata', 'Kolkata'),
    ]
    selected = user_profile.timezones if user_profile.timezones else []

    selected_timezones = {code: label for code, label in all_timezones if code in selected}
    unselected_timezones = {code: label for code, label in all_timezones if code not in selected}

    return render(request, 'main/timezones.html', {
        'selected_timezones': selected_timezones,
        'unselected_timezones': unselected_timezones,
        'all_timezones': all_timezones,
    })

def login_view(request):
    if request.method == 'POST':
        if request.headers.get('Content-Type', '').startswith('application/json'):
            body = request.body.decode('utf-8').strip()
            if not body:
                return JsonResponse({'success': False, 'error': 'Empty request body'})
            try:
                data = json.loads(body)
                username = data.get('username')
                password = data.get('password')
            except json.JSONDecodeError:
                return JsonResponse({'success': False, 'error': 'Invalid JSON'})
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.headers.get('Content-Type', '').startswith('application/json'):
                return JsonResponse({'success': True, 'redirect_url': '/Live-TZ/'})
            else:
                return redirect('/Live-TZ/')
        else:
            if request.headers.get('Content-Type', '').startswith('application/json'):
                return JsonResponse({'success': False, 'error': 'Invalid credentials'})
            else:
                return render(request, 'main/login.html', {'error': 'Invalid credentials'})

    return render(request, 'main/login.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')  # Changed to redirect to the login URL path
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})

from django.contrib.auth import logout

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        request.session.flush()
        return redirect('/login/')
