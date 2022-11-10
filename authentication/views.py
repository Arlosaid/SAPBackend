from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import UserSerializer

# Create your views here.
class RegisterView(APIView):
        def post(self,request):
            serializers= UserSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
    #def _create_user(self, username, email, password):
        # if not email:
        #     raise ValueError('Users must have an email address')

        # user = self.model(
        #     email=self.normalize_email(email),
        #     password=password
        # )
        # user.save(using=self._db)
        # return user

class LoginView(APIView):
    def login_view(request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
        
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
class LogoutView(APIView):
    def logout_view(request):
        logout(request)
# Redirect to a success page.       