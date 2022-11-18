from django.contrib import admin
from .models import EmployeesSubdivision, Divisions, Subdivisions, Employees

# Register your models here.
admin.site.register(Divisions)
admin.site.register(Subdivisions)
admin.site.register(Employees)
admin.site.register(EmployeesSubdivision)