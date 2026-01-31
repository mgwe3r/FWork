from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import User_register_form
from service.models import Service
from django.contrib.auth.decorators import login_required

# Create your views here.

# create login view

# create client_profile and seller_profile 
@login_required
def profile_view(request):
    if request.user.role == "client":
        return render(request, "client/client_profile.html")
    else: 
        fworks = Service.objects.filter(executor=request.user).order_by("-created_at")
        return render(request, "seller/seller_profile.html", {"fworks": fworks})  

    


def register_view(request):
    if request.method == "POST":
        form = User_register_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.role == "client":
                return redirect("profile_view")
            else:
                return redirect("profile_view")
    else:
        form = User_register_form()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.role == "client":
                return redirect("profile_view")
            else:
                return redirect("profile_view")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")
