from django import forms
from .models import Product, Gallery


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
        ]


class GalleryForm(forms.ModelForm):
    image = forms.ImageField(label='Image', widget=forms.ClearableFileInput(
        attrs={
            'blank': 'True',
            'null': 'True',
        }
    ))

    class Meta:
        model = Gallery
        fields = ['image', ]
