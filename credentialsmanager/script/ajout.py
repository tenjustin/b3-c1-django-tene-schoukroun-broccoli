from models import Site

def ajout_site(nom, url, identifiant, mot_de_passe):
    try:
        site = Site(nom=nom, url=url, identifiant=identifiant, mot_de_passe=mot_de_passe)
        site.save()
        return True, "Site ajouté avec succès."
    except Exception as e:
        # Gérer les exceptions
        return False, str(e)