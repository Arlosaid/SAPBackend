from rest_framework import serializers
from .models import *

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'


class EmployeeSubdivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesSubdivision
        fields = ('id_employee','id_subdivison')


class SubdivsionsSerializer(serializers.ModelSerializer):
    employee_items= serializers.SerializerMethodField()

    class Meta:
        model = Subdivisions
        fields = ('id_division','name_subdivision', 'employee_items')

    def get_employee_items(self,obj):
        divisions_query= EmployeesSubdivision.objects.filter(id_subdivison=obj.id)
        serializer= EmployeeSubdivisionSerializer(divisions_query, many=True)

        return serializer.data



