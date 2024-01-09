from django.db import models

class Site(models.Model):
    nom = models.CharField
    url = models.URLField()
    identifiant = models.CharField
    mot_de_passe = models.CharField

    def __str__(self):
        return self.nom
