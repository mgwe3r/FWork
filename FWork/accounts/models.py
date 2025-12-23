from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (("client", "Заказчик"), 
                    ("seller", "Исполнитель"))
    role = models.CharField(choices=ROLE_CHOICES, default="client")
