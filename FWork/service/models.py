from django.db import models
from accounts.models import *

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    executor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"{self.id}-{self.title}-{self.description}-{self.price}"


# Модель Service (services/models.py):

# Поле  Тип  Описание
# title  CharField  Название кворка
# description  TextField  Описание
# price  DecimalField  Цена
# executor  ForeignKey(User)  Исполнитель (роль executor)
# category  CharField  Категория кворка
# created_at  DateTimeField  Дата создания
# updated_at  DateTimeField  Дата редактирования
