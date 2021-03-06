from django.contrib.auth.forms import UserCreationForm

from django import forms

from .models import CustomUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=20, help_text="Email is required")

    class Meta:
        model = CustomUser
        fields = ("email", "user_name", "password1", "password2")
