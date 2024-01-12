from django.contrib import admin
from .models import Site
from .models import CustomUser

admin.site.register(Site)

admin.site.register(CustomUser)

