from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from web_pizza.models import *
from .cart import Cart
from databaseController import DatabaseController

@require_POST
def cart_add(request, name, size):
    cart = Cart(request)
    db = DatabaseController()
    newProd = db.getPruductBySlug(name.strip())
    product = get_object_or_404(Product, id=newProd.get('id'))
    cart.add(product=product, size=size, name=name)
    return redirect('cart:cart_detail')

def cart_remove(request,product_id):
    cart = Cart(request.GET)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart':cart})

def cart_checkout(request):
    cart = Cart(request)
    cart.checkout()
    return render(request, 'checkout.html', {'cart': cart})

def cart_update(request, id, status):
    cart = Cart(request)
    cart.update(id, status)
    return redirect('web_pizza:cook')
