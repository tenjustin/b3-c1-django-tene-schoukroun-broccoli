from django.urls import path
from . import views

urlpatterns = [
    path("", views.liste_sites, name="liste_sites"),
    path("supprimer/<int:pk>/", views.supprimer_enregistrement, name='supprimer_enregistrement'),
    path("modification_site/<int:pk>/", views.modifier_site, name="modification_site"),
    path("ajout_site", views.ajout_site_action, name="ajout_site"),
    path('export-csv/', views.exporter_identifiants_csv, name='export_csv'),
    path('import-csv/', views.import_csv, name='import_csv'),
    path('page-import/', views.page_import, name='page_import')
]
