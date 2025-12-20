from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class User_register_form(UserCreationForm):
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        label="Кто вы"
    )

    class Meta():
        model = User
        fields = ["username", "email", "password", "password_check", "role", "phonenumbers"]