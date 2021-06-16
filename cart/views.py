from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from web_pizza.models import *
from mystore.forms import CustomerForm
from cart.forms import *
from .cart import Cart
from databaseController import DatabaseController

@require_POST
def cart_add(request, name, size):
    cart = Cart(request)
    db = DatabaseController()
    newProd = db.getPruductBySlug(name.strip())
    product = get_object_or_404(Product, id=newProd.get('id'))
    formToppings = toppings
    # if formToppings.is_valid():
    #     Cheese = formToppings.cleaned_data['Cheese']
    #     Pepperoni = formToppings.cleaned_data['Pepperoni']
    #     Mushrooms = formToppings.cleaned_data['Mushrooms']
    #     Sausage = formToppings.cleaned_data['Sausage']
    #     Onions = formToppings.cleaned_data['Onions']
    #     Bacon = formToppings.cleaned_data['Bacon']
    #     Peppers = formToppings.cleaned_data['Peppers']
    #     Black_Olives = formToppings.cleaned_data['Black_Olives']
    #     Chicken = formToppings.cleaned_data['Chicken']
    #     Pineapple = formToppings.cleaned_data['Pineapple']
    #     Spinach = formToppings.cleaned_data['Spinach']
    #     Basil = formToppings.cleaned_data['Basil']
    #     Ham = formToppings.cleaned_data['Ham']
    #     Pesto = formToppings.cleaned_data['Pesto']
    #     Beef = formToppings.cleaned_data['Beef']
    #     Artichoke = formToppings.cleaned_data['Artichoke']
    #     Anchovies = formToppings.cleaned_data['Anchovies']
    #     Tomatoes = formToppings.cleaned_data['Tomatoes']
    #     SunDried_Tomatoes = formToppings.cleaned_data['SunDried_Tomatoes']
    cart.add(product=product, size=size, name=name)
    return redirect('cart:cart_detail')

def cart_remove(request, name):
    cart = Cart(request)
    db = DatabaseController()
    prod = db.getOrderItem(name)
    cart.remove(prod)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    form = customerInfo()
    return render(request, 'cart/detail.html', {'cart':cart, 'form':form})

def cart_checkout(request):
    cart = Cart(request)
    cart.checkout()
    return render(request, 'checkout.html', {'cart': cart})

def cart_update(request, id, status):
    cart = Cart(request)
    cart.update(id, status)
    return redirect('web_pizza:cook')
