from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
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