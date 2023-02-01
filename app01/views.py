from django.http import HttpResponse
from django.template import loader

from .models import db01


def hello(request):
    return HttpResponse("Hello world!")


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def membres(request):
  membres = db01.objects.all().values()
  template = loader.get_template('membres.html')
  context = {
    'membres': membres,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  membres = db01.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'membres': membres,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
  

