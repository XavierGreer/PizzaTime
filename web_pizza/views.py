from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from .models import *
from cart.forms import CartAddProductForm

def index(request):
    template = loader.get_template('home.html')  # getting our template
    return HttpResponse(template.render())  # rendering the template in HttpResponse

def menu(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'menu.html', {'category':category,'cartegories':categories,'products':products})

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

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

