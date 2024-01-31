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

def detail_site(request, pk):
    site = get_object_or_404(Site, pk=pk)
    return render(request, 'details_site.html', {'site': site})

def liste_sites(request):
    query = request.GET.get('q')

    if query:
        sites = Site.objects.filter(nom__icontains=query)
    else:
        sites = Site.objects.all()

    return render(request, 'index.html', {'sites': sites, 'query': query})

def ajout_site_action(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        url = request.POST.get('url')
        identifiant = request.POST.get('identifiant')
        mot_de_passe = request.POST.get('mot_de_passe')
        success, message = ajout.ajout_site(nom, url, identifiant, mot_de_passe)
        if success:
            return redirect('/passmanager/')  
        else:
            return render(request, 'error.html', {'message': message})
    else:
        form = SiteForm()
    return render(request, 'ajout_site.html', {'form': form})
    
def supprimer_enregistrement(request, pk):
    objet_a_supprimer = get_object_or_404(Site, pk=pk)
    objet_a_supprimer.delete()
    return redirect('liste_sites')

def generer_mot_de_passe():
    length = 12  
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for i in range(length))

def modifier_site(request, pk):
    site = get_object_or_404(Site, pk=pk)

    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('liste_sites')  
    else:
        form = SiteForm(instance=site)

    return render(request, 'modifier_site.html', {'form': form})