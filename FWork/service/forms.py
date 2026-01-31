from django import forms
from service.models import *

class Service_Creation_Form(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["title", "description", "price", "category"]