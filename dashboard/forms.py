from attr import field
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"