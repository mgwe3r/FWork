from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from service.forms import Service_Creation_Form
from service.models import Service

# Create your views here.

@login_required
def service_create(request):
    form = Service_Creation_Form()
    if request.method == "POST":
        form = Service_Creation_Form(request.POST)
        if form.is_valid():
            order = form.save()
            order.executor = request.user
            order.save()
            return redirect("profile_view")
        else:
            form = Service_Creation_Form()

    return render(request, "order_page.html", {"form": form})   

def fworks(request, fwork_id):
    fwork = get_object_or_404(Service, id=fwork_id)
    return render(request, "fwork_page.html", {"fwork": fwork})