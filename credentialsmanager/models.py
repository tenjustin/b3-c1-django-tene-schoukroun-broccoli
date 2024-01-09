from typing import Any
from django.db import models

class Site(models.Model):
    nom = models.CharField
    url = models.URLField()
    identifiant = models.CharField
    mot_de_passe = models.CharField
    
    def __init__(self, nom, url, identifiant, mot_de_passe):
        self.nom = nom
        self.url = url
        self.identifiant = identifiant
        self.mot_de_passe = mot_de_passe

    def __str__(self):
        return self.nom
