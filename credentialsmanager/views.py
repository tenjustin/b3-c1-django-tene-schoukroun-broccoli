from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from .models import Site
from .forms import SiteForm

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


def liste_sites(request):
    sites = Site.objects.all()
    return render(request, 'liste_sites.html', {'sites': sites})

def ajout_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_sites')
    else:
        form = SiteForm()
    return render(request, 'ajout_site.html', {'form': form})