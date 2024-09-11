from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from account.forms import LoginForm, SignupForm


def user_signup(request):
    on_error = False
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            registration_token = form.cleaned_data.get("registration_token")
            if registration_token == settings.REGISTRATION_TOKEN:
                user = form.save()
                user.is_superuser = True
                user.save()
                return redirect("login")
            else:
                on_error = True
    else:
        form = SignupForm()
    return render(request, "pages/auth/register.html", {"form": form, "on_error": on_error})


def user_login(request):
    on_error = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect("customer_list")
            else:
                on_error = True
    else:
        form = LoginForm()
    return render(request, "pages/auth/login.html", {"form": form, "on_error": on_error})


def user_logout(request):
    logout(request)
    return redirect("login")
