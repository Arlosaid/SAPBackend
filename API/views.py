from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from .models import *
from .serializers import EmployeeSerializers

# Create your views here.
class GetView(APIView):
    def get(self, request):
        queryset= Employees.objects.all()
        print(queryset)
        serializer= EmployeeSerializers(queryset, many=True)
        serialized_data= serializer.data
        return Response(serialized_data, status=200)

class SaveView(APIView):
    def post(self,request):
        serializer= EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

        return Response(serializer.data, status=200)

class UpdateView(APIView):
    def put(self,request, pk):
        data= request.data
        user= Employees.objects.get(id=pk)
        serializer= EmployeeSerializers(instance=user, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)

class DeleteView(APIView):
    def delete(self, request, pk):
        try:
            user= Employees.objects.get(id=pk)
            if user:
                user.delete()
                return Response({"msg":"Eliminado correctamente"}, status=200)
        except:
            return Response({"msg":"No se encontró el usuario"}, status=404)

