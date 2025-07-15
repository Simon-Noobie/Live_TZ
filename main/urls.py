from django.contrib import auth,admin
from django.urls import path
from main.views import timezones_view, register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Live-TZ/', timezones_view, name='timezones'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
