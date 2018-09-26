from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "category",
            "price_per_day",
            "price_per_week",
            "price_per_month",
            "price_per_year",
            "location",
            "phone_number",
            "health",
            "image",
        ]
