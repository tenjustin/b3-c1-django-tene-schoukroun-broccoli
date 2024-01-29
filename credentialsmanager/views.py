from django.shortcuts import get_object_or_404, render, redirect
from .models import Site
from .forms import SiteForm
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Site
from django.shortcuts import render, redirect
from .forms import SiteForm
from credentialsmanager.script import ajout

# Create your views here.
# views.py

def liste_sites(request):
    sites = Site.objects.all()
    return render(request, 'index.html', {'sites': sites})

def ajout_site_action(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        url = request.POST.get('url')
        identifiant = request.POST.get('identifiant')
        mot_de_passe = request.POST.get('mot_de_passe')
        success, message = ajout.ajout_site(nom, url, identifiant, mot_de_passe)
        if success:
            return redirect('/passmanager/')  # Rediriger vers une URL de succès
        else:
            return render(request, 'error.html', {'message': message})
    else:
        form = SiteForm()
    return render(request, 'ajout_site.html', {'form': form})
    
def supprimer_enregistrement(request, pk):
    objet_a_supprimer = get_object_or_404(Site, pk=pk)
    objet_a_supprimer.delete()
    return redirect('liste_sites')
