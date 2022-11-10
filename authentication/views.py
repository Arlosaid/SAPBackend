from django.shortcuts import render
from django.contrib.auth import  login, logout
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.authtoken.models import Token

from authentication.models import CustomUser


# Create your views here.
class RegisterView(APIView):
    '''Registrar usuario'''
    def post(self,request):
        email = request.data['email']
        password = make_password(request.data['password'])
        first_name = request.data['first_name']  
        last_name = request.data['last_name']  
        
        try:
            user = CustomUser.objects.create(email=email,password=password,first_name=first_name,last_name=last_name)
            Token.objects.create(user=user)
            mensaje = {"msg":"Usuario registrado"}
            estado = status.HTTP_201_CREATED
        except Exception as err:
            print(err)
            mensaje = {"msg":"No se pudo registrar el usuario"}
            estado = status.HTTP_400_BAD_REQUEST
        return Response(mensaje,estado)
           


class LoginView(APIView):
    '''Logear usuario'''
    def login_view(self,request):
        email = request.data['email']
        password = request.data['password']
        email = email.replace(" ", "")
              
        try:
            user = CustomUser.objects.get(email=email)
            pass_user = user.password
            check_pass = check_password(password,pass_user)
                    
        except:
            check_pass = False
        
        
        
         
        # if user is not None:
        #     login(request, user)
        # Redirect to a success page.
        
        
        
class LogoutView(APIView):
    '''Logout usuario'''
    def logout_view(request):
        logout(request)
# Redirect to a success page.       