from django.contrib import auth,admin
from django.urls import path
from main.views import timezones_view, register_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', timezones_view, name='timezones'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
