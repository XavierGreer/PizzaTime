from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render('about.html'))
    return render(request, 'about.html')