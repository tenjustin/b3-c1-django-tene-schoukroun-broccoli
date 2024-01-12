from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from .models import Site

# Create your views here.

def index(request):
    password_list = []
    password_list.append(Site(1, "example", "example.com", "Justin", "Password123"))
    template = loader.get_template("index.html")
    context = {
        "password_list": password_list,
    }
    return HttpResponse(template.render(context, request))

def supprimer_enregistrement(request, pk):
    objet_a_supprimer = get_object_or_404(Site, pk=pk)
    objet_a_supprimer.delete()
    return redirect('index')