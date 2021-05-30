from django import forms
from web_pizza.models import OrderItem

PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range(1,10)]
class CartAddProductForm(forms.Form):
    PRODUCT_PIZZA_SIZE =  (
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    )

    SIDESIZES = (
        ("Small", "Small"),
        ("Medium", "Medium"),
    )
    sidesize = forms.ChoiceField(choices=SIDESIZES)

    SODASIZES = (
        ("Small", "Small"),
        ("Medium", "Medium"),
    )
    sodasize = forms.ChoiceField(choices=SODASIZES)

    pizzasize = forms.TypedChoiceField(choices=PRODUCT_PIZZA_SIZE)





    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

'''class CartAddProductForm(forms.ModelForm):
    class Meta:
        model= OrderItem
        fields= ["price"]'''