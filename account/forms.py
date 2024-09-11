from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import User


class SignupForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    registration_token = forms.CharField(required=True, max_length=100, help_text="Enter your promo code (optional)")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
