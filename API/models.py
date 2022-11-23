from django.db import models
from authentication.models import CustomUser            

# Create your models here.
class Divisions(models.Model):
    name_division= models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name_division}"

class Subdivisions(models.Model):
    id_division= models.ForeignKey(Divisions, on_delete=models.DO_NOTHING)
    name_subdivision= models.CharField(max_length=25)

    def __str__(self):
        return f"{self.id_division}, {self.name_subdivision}"


class Employees(models.Model):
    user= models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    phone= models.IntegerField(unique=True)
    url_photo= models.URLField(max_length=255)
    biography= models.TextField(blank=True, null=True)
    data_entry= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}, {self.phone}, {self.url_photo}, {self.biography}, {self.data_entry}"

class EmployeesSubdivision(models.Model):
    id_employee = models.ForeignKey(Employees, on_delete=models.DO_NOTHING)    
    id_subdivision = models.ForeignKey(Subdivisions, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.id_employee}, {self.id_subdivision}"






