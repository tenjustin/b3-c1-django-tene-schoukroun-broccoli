import csv
from django.shortcuts import get_object_or_404, render, redirect
from .models import CustomUser, Site
from .forms import SiteForm
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Site
from django.shortcuts import render, redirect
from .forms import SiteForm
from credentialsmanager.script import ajout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

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

def page_import(request):
    return render(request, 'page_import.html')

def import_csv(request):
    if request.method == 'POST' and 'file' in request.FILES:
        csv_file = request.FILES['file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()

        # Utiliser le module CSV pour lire les données du fichier
        reader = csv.reader(decoded_file)
        
        first_row = True         
         
        for row in reader:
            if first_row:
                first_row = False
                continue
            # Traiter chaque ligne et enregistrer les données dans le modèle Django
            obj, created = Site.objects.get_or_create(nom=row[0], url=row[1], identifiant=row[2], mot_de_passe=row[3])  # ajustez en fonction de votre modèle
            obj.save()

        return redirect(liste_sites)

    return redirect(liste_sites)

def exporter_identifiants_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="identifiants.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nom du site','URL', 'Identifiant', 'Mot de passe'])  # En-têtes CSV

    identifiant = Site.objects.all()  # Récupérer les mots de passe depuis le modèle Django

    for identifiant in identifiant:
        writer.writerow([identifiant.nom, identifiant.url,identifiant.identifiant, identifiant.mot_de_passe])

    return response

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