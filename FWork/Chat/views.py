from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from orders.models import Order
from Chat.models import ChatMessage
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def chat_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.user != order.client and request.user != order.service.executor:
        return redirect("profile_view")
    
    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            ChatMessage.objects.create(
                order=order,
                sender=request.user,
                text=text,
            )
        return redirect("chat_view", order_id=order.id)
    messages = order.message.order_by("created_at")
    return render(request, "chat/order_chat.html", {"order":order,
                                                    "messages":messages})
