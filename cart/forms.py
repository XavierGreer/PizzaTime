from django import forms
from web_pizza.models import *

PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range(1,10)]
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(required=False, choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
