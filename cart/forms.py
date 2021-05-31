from django import forms
from web_pizza.models import *


PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range(1,10)]
class CartAddProductForm(forms.Form):

    size = forms.ChoiceField(choices=PIZZA_SIZES, label='Size')

    price = 1
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    if size == 'Large':
        price = Product.priceLg

class checkoutForm(forms.Form):

    size = forms.ChoiceField(choices=PIZZA_SIZES, label='Size')