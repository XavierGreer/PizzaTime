from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from web_pizza.models import *
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],override_quantity=cd['override'])
    return redirect('cart:cart_detail')

def cart_remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity':item['quantity'], 'override':True})
    return render(request, 'cart/detail.html',{'cart':cart})

def cart_checkout(request):
    '''cart = Cart(request)
    order = Order.objects.all

    if request.method == "POST":
        if cart.is_valid():
            cart.save()
        return render(request, 'checkout.html', {order:"order"})
    else:
        return render(request, 'checkout.html', {order:"order"})'''

    cart = Cart(request)
    return render(request, 'checkout.html', {'cart': cart})
