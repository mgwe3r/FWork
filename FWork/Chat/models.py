from django.db import models
from orders.models import Order
from accounts.models import User

# Create your models here.
class ChatMessage(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="message", blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}-{self.created_at}"