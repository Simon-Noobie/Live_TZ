from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

TIMEZONE_CHOICES = [
    ('UTC', 'UTC'),
    ('New York', 'New York'),
    ('London', 'London'),
    ('Kolkata', 'Kolkata'),
]

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    timezones = forms.MultipleChoiceField(
        choices=TIMEZONE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'timezones']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        profile = super().save(commit=False)
        profile.user = user
        profile.email = self.cleaned_data['email']
        profile.name = self.cleaned_data['name']
        profile.password = user.password  # hashed password
        profile.timezones = self.cleaned_data['timezones']
        if commit:
            profile.save()
        return profile
