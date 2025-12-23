from django.shortcuts import render
from accounts.forms import User_register_form

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = User_register_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = User_register_form()
    return render(request, "accounts/register.html", {"form": form})

# сделать register_view