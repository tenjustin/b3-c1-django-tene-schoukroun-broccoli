from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/ajout_site", views.ajout_site_action, name="ajout_site"),
]
