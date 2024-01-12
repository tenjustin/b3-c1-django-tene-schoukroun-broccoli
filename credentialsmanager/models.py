from typing import Any
from django.db import models


class Site(models.Model):
    nom = models.CharField(max_length=200, default='')
    url = models.URLField()
    identifiant = models.CharField(max_length=200, default='')
    mot_de_passe = models.CharField(max_length=200, default='')
    

    def __str__(self):
        return self.nom
    
class CustomUser(models.Model):
    identifiant = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)

    def __str__(self):
        return self.username
