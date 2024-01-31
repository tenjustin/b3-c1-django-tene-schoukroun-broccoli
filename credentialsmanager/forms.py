# forms.py
from django import forms
from .models import Site  

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site  
        fields = ['nom', 'url', 'identifiant', 'mot_de_passe']  
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'identifiant': forms.TextInput(attrs={'class': 'form-control'}),
            'mot_de_passe': forms.PasswordInput(attrs={'class': 'form-control'}),
        }