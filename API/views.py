from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import *
from .serializers import EmployeeSerializers, EmployeeSubdivisionSerializer, EmployeeUpdateSerializers
from django.db.models import Q

# Create your views here.
class GetAllEmployeesView(APIView):
    permission_classes= (IsAdminUser,)
    def get(self, request):
        queryset= Employees.objects.all()
        print(queryset)
        serializer= EmployeeSerializers(queryset, many=True)
        serialized_data= serializer.data
        return Response(serialized_data, status.HTTP_200_OK)

class GetEmployeesDivisionsDetailsView(APIView):
    permission_classes= (IsAdminUser,)
    def get(self,request):
        queryset = EmployeesSubdivision.objects.all()
        serializer = EmployeeSubdivisionSerializer(queryset, many=True)
        serializer_data = serializer.data
        return Response(serializer_data, status.HTTP_200_OK)

class CreateNewEmployeeView(APIView):
    permission_classes= (IsAdminUser,)
    def post(self,request):
        serializer= EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

        return Response(serializer.data, status.HTTP_201_CREATED)

        
class DeleteEmployeeView(APIView):
    permission_classes= (IsAdminUser,)
    def delete(self, request, pk):
        try:
            user= Employees.objects.get(id=pk)
            if user:
                user.delete()
                return Response({"msg":"Successfully deleted"}, status.HTTP_200_OK)
        except:
            return Response({"msg":"User was not found"}, status.HTTP_404_NOT_FOUND)

class UpdateEmployeeInfo(APIView):
    def put(self, request):
        name = request.data["name"]
        last_name = request.data["last_name"]
        phone = request.data["phone"]
        email = request.data["email"]
        #division = request.data["division"]
        subdivision = request.data["subdivision"]

        # employee_name = 
        
        employee_email = CustomUser.objects.get(email=email)
        if employee_email:
            employee_email.first_name = name
            employee_email.save()
            employee_email.last_name = last_name
            employee_email.save()
        
        employee = Employees.objects.get(user=employee_email)
        if employee:
            employee.phone = phone
            employee.save()


        sub= Subdivisions.objects.get(pk=subdivision)
        employee_id = EmployeesSubdivision.objects.get(id_employee= employee)
        if employee_id:
            employee_id.id_subdivision= sub
            employee_id.save()

            print(employee_id)
        return Response({"msg":"ok"}, status.HTTP_200_OK)