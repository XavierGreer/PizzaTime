from django.shortcuts import render,get_object_or_404,redirect
from .cart import Cart
from django.views.decorators.http import require_POST
from web_pizza.models import Product
from .forms import CartAddProductForm

@require_POST
def cart_add(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm
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
    return render(request, 'cart/detail.html',{'cart':cart})