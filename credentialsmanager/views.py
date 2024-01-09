from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from credentialsmanager.models import Site
from credentialsmanager.scripts import delete

# Create your views here.

def index(request):
    password_list = []
    password_list.append(Site("example", "example.com", "Justin", "Password123"))
    template = loader.get_template("index.html")
    context = {
        "password_list": password_list,
    }
    return HttpResponse(template.render(context, request))

def delete_action(request):
    if request.method == 'POST':
        delete.run_delete()  # Supposons que run_delete() est une fonction dans delete.py
        # Rediriger ou afficher un message de succès
        return render(request, 'index.html')
    else:
        # Gérer les autres méthodes (GET, etc.)
        return render(request, 'error.html')