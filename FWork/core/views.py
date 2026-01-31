from django.shortcuts import render, redirect
from service.models import Service
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    fworks = Service.objects.all().order_by('-created_at')
    return render(request, "main_page.html", {"fworks": fworks})