from django.shortcuts import render

# Create your views here.
def timezones_view(request):
    return render(request, 'main/timezones.html')
