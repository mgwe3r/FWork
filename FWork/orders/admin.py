from django.contrib import admin
from .models import *


@admin.register(Order)

class Order_admin(admin.ModelAdmin):
    list_display = ("id", "status", "client")
