from django.db import models
from accounts.models import *
from service.models import *

class Order(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # status = models.CharField(max_length=100)
    # description = models.TextField(blank=True, null=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client.username}-{self.service.title}"

# Заказы

# Модель Order (orders/models.py):

# Поле  Тип  Описание
# service  ForeignKey(Service)  Кворк, который заказали
# client  ForeignKey(User)  Заказчик (роль client)
# status  CharField  Статус: new, in_progress, completed
# created_at  DateTimeField  Дата заказа
# updated_at  DateTimeField  Дата обновления статуса
