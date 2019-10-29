from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Snippet

from .models import Project

admin.site.register(Project)

admin.site.site_header = 'Timur Makarov Dashboard'
admin.site.register(Snippet)