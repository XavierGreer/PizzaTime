from django.shortcuts import render
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from databaseController import DatabaseController
from django.contrib import messages
from django.views.generic.base import RedirectView
from .models import *

def index(request):
    return render(request, 'home.html')

def menu(request):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    context = {'cartegories':categories, 'products':products}
    return render(request, 'menu.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    db = DatabaseController()
    name = db.getProductByName(product.name)
    return render(request, 'detail.html',
              {'product':product, 'name':name[0][3], 'priceSm':name[0][8], 'priceMd':name[0][9], 'priceLg':name[0][10], 'idNum':name[0][0]})

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
    orders = Order.objects.all()
    orderItems =OrderItem.objects.all()
    return render(request, 'cook.html', {'orders':orders})
