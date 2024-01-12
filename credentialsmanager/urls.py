from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/ajout_site.html", views.ajout_site, name="ajout_site"),
]
