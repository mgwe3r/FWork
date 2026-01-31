from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('register/', views.register_view, name="register_view"),
    path("client_profile/", views.profile_view, name="profile_view"),
    path("seller_profile/", views.profile_view, name="profile_view"),
    path("login/", views.login_view, name="login_view"),
    path("logout/", views.logout_view, name="logout_view")
]