from django.contrib import admin
from Chat.models import ChatMessage

# Register your models here.

@admin.register(ChatMessage)

class Chat_Admin(admin.ModelAdmin):
    list_display = ("sender", "text")