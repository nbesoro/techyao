from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from account.forms import LoginForm


def user_login(request):
    on_error = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print("yes")
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect("customer_list")
            else:
                on_error = True
        else:
            print("no")
    else:
        form = LoginForm()
    return render(request, "pages/auth/login.html", {"form": form, "on_error": on_error})


def user_logout(request):
    logout(request)
    return redirect("login")
