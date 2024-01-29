from django.contrib import admin

from credentialsmanager.models import Site
from .models import Site
from .models import CustomUser

admin.site.register(Site)

admin.site.register(CustomUser)


admin.site.register(Site)