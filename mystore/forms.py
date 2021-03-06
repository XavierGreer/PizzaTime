from django import forms
from web_pizza.models import Topping, Pizza, Soda, Side, Product, Customer, Order


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'firstname',
            'lastname',
            'phone',
            'email',
            'address',
            'zipcode'
        ]
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'customer',
            'status',
            'total',
            'tax',
            'discount'
        ]

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = [
            'name'
        ]

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'product_type',
            'name',
            'image',
            'priceSm',
            'priceMd',
            'priceLg',
        ]

class SodaForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'product_type',
            'name',
            'image',
            'priceSm',
            'priceLg'
        ]

class SideForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'product_type',
            'name',
            'image',
            'priceSide'
        ]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_type',
            'name',
            'image',
            'priceSm',
            'priceMd',
            'priceLg',
            'priceSide',
        ]