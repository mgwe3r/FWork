from django.contrib import admin
from accounts.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here

@admin.register(User)

class User_Admin(UserAdmin):
    list_display = ("username", "email", "role")
