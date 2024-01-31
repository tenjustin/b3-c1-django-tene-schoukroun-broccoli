from django.urls import path
from . import views

urlpatterns = [
    path("", views.liste_sites, name="liste_sites"),
    path("supprimer/<int:pk>/", views.supprimer_enregistrement, name='supprimer_enregistrement'),
    path("ajout_site/", views.ajout_site_action, name="ajout_site"),
    path("modification_site/<int:pk>/", views.modifier_site, name="modification_site"),
    path('detail_site/<int:pk>/', views.detail_site, name='detail_site'),

]
