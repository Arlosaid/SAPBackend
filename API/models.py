from django.db import models

# Create your models here.
class Roles(models.Model):
    name_role= models.CharField(max_length=25)

    def __str__(self):
        return self.name_role

class Divisions(models.Model):
    name_division= models.CharField(max_length=25)

    def __str__(self):
        return self.name_division

class Subdivisions(models.Model):
    id_division= models.ForeignKey(Divisions, on_delete=models.DO_NOTHING)
    name_subdivision= models.CharField(max_length=25)

    def __str__(self):
        return self.name_subdivision


class Employees(models.Model):
    name= models.CharField(max_length=80)
    surname= models.CharField(max_length=80)
    id_role= models.ForeignKey(Roles, on_delete=models.DO_NOTHING)
    phone= models.IntegerField(unique=True)
    email= models.EmailField(max_length=50, unique=True)
    password= models.CharField(max_length=255)
    url_photo= models.URLField(max_length=255)
    biography= models.TextField(blank=True, null=True)
    data_entry= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.surname

class EmployeesSubdivisions(models.Model):
    id_employee= models.ForeignKey(Employees, on_delete=models.DO_NOTHING)
    id_subdivision= models.ForeignKey(Subdivisions, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id_subdivision) + " " + str(self.id_employee)
        







