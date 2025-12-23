from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('register/', views.register_view, name="register_view"),
]