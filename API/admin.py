from django.contrib import admin
from .models import Roles, Divisions, Subdivisions, Employees

# Register your models here.
admin.site.register(Roles)
admin.site.register(Divisions)
admin.site.register(Subdivisions)
admin.site.register(Employees)