from django.contrib import admin
from .models import *

@admin.register(Service)

class Service_admin(admin.ModelAdmin):
    list_display = ("id", "title", "price")
