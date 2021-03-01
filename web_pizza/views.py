from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('home.html')  # getting our template
    return HttpResponse(template.render())       # rendering the template in HttpResponse