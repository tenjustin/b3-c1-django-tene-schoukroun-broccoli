from django.contrib import admin

from credentialsmanager.models import Site
from .models import Site

admin.site.register(Site)