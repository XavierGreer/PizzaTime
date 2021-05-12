from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())