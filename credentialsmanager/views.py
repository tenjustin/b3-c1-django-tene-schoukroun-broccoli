from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Site

# Create your views here.

def index(request):
    password_list = []
    password_list.append(Site("example", "example.com", "Justin", "Password123"))
    template = loader.get_template("index.html")
    context = {
        "password_list": password_list,
    }
    return HttpResponse(template.render(context, request))