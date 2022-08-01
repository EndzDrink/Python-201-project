from django.contrib import admin
from .models import Profiles

class ProfilesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profiles, ProfilesAdmin)

