from typing import Any
from typing import Any
from django.db import models
from django.urls import reverse


class Site(models.Model):
    id = models.Index
    nom = models.CharField(max_length=255,default="")
    url = models.URLField()
    identifiant = models.CharField(max_length=255,default="")
    mot_de_passe = models.CharField(max_length=255,default="")
    
    # def __init__(self, id, nom, url, identifiant, mot_de_passe):
    #     self.id = id
    #     self.nom = nom
    #     self.url = url
    #     self.identifiant = identifiant
    #     self.mot_de_passe = mot_de_passe

    def __str__(self):
        return self.nom
    
    def get_absolute_url(self):
        return reverse('', args=[str(self.id)])
    
class CustomUser(models.Model):
    identifiant = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)

    def __str__(self):
        return self.username
