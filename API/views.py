from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from .models import *
from .serializers import EmployeeSerializers, EmployeeSubdivisionSerializer, SubdivsionsSerializer
from django.db.models import Q

# Create your views here.
class GetView(APIView):
    def get(self, request):
        queryset= Employees.objects.all()
        print(queryset)
        serializer= EmployeeSerializers(queryset, many=True)
        serialized_data= serializer.data
        return Response(serialized_data, status.HTTP_200_OK)

class GetEmployeesSubdivisionView(APIView):
        def get(self,request):
            queryset = Subdivisions.objects.all()
            serializer = SubdivsionsSerializer(queryset, many=True)
            serializer_data = serializer.data
            return Response(serializer_data, status.HTTP_200_OK)

class SaveView(APIView):
    def post(self,request):
        serializer= EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

        return Response(serializer.data, status.HTTP_201_CREATED)

class UpdateView(APIView):
    def put(self,request, pk):
        data= request.data
        user= Employees.objects.get(id=pk)
        serializer= EmployeeSerializers(instance=user, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_404_NOT_FOUND)


class DeleteView(APIView):
    def delete(self, request, pk):
        try:
            user= Employees.objects.get(id=pk)
            if user:
                user.delete()
                return Response({"msg":"Successfully deleted"}, status.HTTP_200_OK)
        except:
            return Response({"msg":"User was not found"}, status.HTTP_404_NOT_FOUND)

