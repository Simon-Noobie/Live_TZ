from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=128)  # same length Django uses for hashed passwords
    timezones = JSONField(default=list, blank=True)

    def __str__(self):
        return self.user.username
# Create your models here.
