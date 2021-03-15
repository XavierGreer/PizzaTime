from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView

def index(request):
    template = loader.get_template('home.html')  # getting our template
    return HttpResponse(template.render())       # rendering the template in HttpResponse

def menu(request):
    template = loader.get_template('menu.html')  # getting our template
    return HttpResponse(template.render())       # rendering the template in HttpResponse

class ArticleCounterRedirectView(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'menu'

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(menu, pk=kwargs['pk'])
        article.update_counter()
        return super().get_redirect_url(*args, **kwargs)