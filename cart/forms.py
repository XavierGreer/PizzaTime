from django import forms

PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range(1,10)]
class productQuantity(forms.Form):
    quantity = forms.TypedChoiceField(required=False, choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class toppings(forms.Form):
    CHOICES = (('None','None'),
               ('Extra','Extra'),)
    Cheese = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Pepperoni = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Mushrooms = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Sausage = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Onions = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Bacon = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Peppers = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Black_Olives = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Chicken = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Pineapple = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Spinach = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Basil = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Ham = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Pesto = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Beef = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Artichoke = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Spinach = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Anchovies = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    Tomatoes = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')
    SunDried_Tomatoes = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial= 'None')

class customerInfo(forms.Form):
    name = forms.CharField(label='Name', required=True)
    number = forms.CharField(label='Name', required=True)