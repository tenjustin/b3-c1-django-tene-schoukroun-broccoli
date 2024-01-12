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

# views.py
from django.shortcuts import render, redirect
from .forms import SiteForm

def ajout_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = SiteForm()

    return render(request, 'ajout_site.html', {'form': form})
