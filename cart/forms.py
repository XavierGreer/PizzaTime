from django import forms
from web_pizza.models import *

PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range(1,10)]

# class CartAddProductForm(forms.Form):
#     size = forms.ChoiceField(required=False, choices=PIZZA_SIZES, label='Size', initial='Large')
#     #size = forms.ChoiceField(widget=forms.Select(), choices=PIZZA_SIZES)
#     quantity = forms.TypedChoiceField(required=False, choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
#     override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class CartAddProductForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = []