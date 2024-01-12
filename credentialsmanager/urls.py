from django.urls import path

from . import views

urlpatterns = [
    path("/", views.index, name="index"),
    path('/supprimer/<int:pk>/', views.supprimer_enregistrement, name='supprimer_enregistrement'),
]