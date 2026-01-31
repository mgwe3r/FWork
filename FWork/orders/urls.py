from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path("create/<int:service_id>", views.create_order, name="create_order"),
    path("seller_orders/", views.seller_orders_view, name="seller_orders_view"),
    path("client_orders/", views.client_orders_view, name="client_orders_view"),
]