from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from .models import Category, Product
from cart.forms import CartAddProductForm


def index(request):
    template = loader.get_template('home.html')  # getting our template
    return HttpResponse(template.render())  # rendering the template in HttpResponse


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'menu.html', {'category': category, 'categories': categories, 'products': products})

    '''template = loader.get_template('menu.html')  getting our template
    return HttpResponse(template.render())        rendering the template in HttpResponse'''


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'pizza_time/templates/detail.html',
                  {'product': product, 'cart_product_form': cart_product_form})


class ArticleCounterRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'product_list'

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(product_list, pk=kwargs['pk'])
        article.update_counter()
        return super().get_redirect_url(*args, **kwargs)
