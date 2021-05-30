from django.shortcuts import render
from django.template.loader import get_template
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from .models import *
import user.views
from cart.forms import CartAddProductForm

def index(request):
    #template = loader.get_template('base.html')  # getting our template
    #return HttpResponse(template.render())  # rendering the template in HttpResponse
    return render(request, 'home.html')

"""def menu(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    context = {'category':category,'cartegories':categories,'products':products}
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'menu.html', context)"""

def menu(request):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    context = {'cartegories':categories,'products':products}
    return render(request,'menu.html', context)

def product_detail(request, id, slug):
    cart_product_form = CartAddProductForm()
    product = get_object_or_404(Product, id=id,slug=slug,available=True)
    return render(request, 'detail.html',
                  {'product':product, 'cart_product_form':cart_product_form})

class ArticleCounterRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'menu'

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(menu, pk=kwargs['pk'])
        article.update_counter()
        return super().get_redirect_url(*args, **kwargs)

def aboutus(request):
    return render(request, 'about.html')

def cookorder(request):
    orders = Order.objects.all
    return render(request, 'cook.html', {'orders':orders})