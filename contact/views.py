from django.template import loader
from django.http import HttpResponse

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())