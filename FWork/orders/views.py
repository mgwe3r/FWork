from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from orders.models import Order
from service.models import Service
from django.contrib.auth.decorators import login_required

# Create your views here.



@login_required
def client_orders_view(request):
    orders = Order.objects.filter(client=request.user)
    return render(request, "client/client_orders.html", {"orders":orders})

@login_required
def seller_orders_view(request):
    orders = Order.objects.filter(service__executor=request.user)
    return render(request, "seller/seller_orders.html", {"orders":orders})


@login_required
def create_order(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.user == service.executor:
        return redirect("fworks")
    
    if Order.objects.filter(service=service, client=request.user).exists():
        return redirect("fworks")
    
    Order.objects.create(service=service, client=request.user)
    return redirect("chat_view", fwork_id=fwork.id)



