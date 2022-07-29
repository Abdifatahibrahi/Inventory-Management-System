from attr import field
from django import forms
from .models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["product", "order_quantity"]