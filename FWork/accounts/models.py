from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (("client", "заказчик"), 
                    ("seller", "исполнитель"))
    role = models.CharField(choices=ROLE_CHOICES, default="client")
