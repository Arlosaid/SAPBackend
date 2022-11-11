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
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        email = email.replace(" ", "")
              
        try:
            user = CustomUser.objects.get(email=email)
            pass_user = user.password
            check_pass = check_password(password,pass_user)

                    
        except:
            check_pass = False
        
        if check_pass:
            try:
                token= Token.objects.get(user=user)


            except Token.DoesNotExist:
                token= Token.objects.create(user=user)
            data= {"msg":"Accepted","id":user.id,"first_name": user.first_name,"last_name":user.last_name,"email":user.email,"token":str(token.key)}
            estado= status.HTTP_202_ACCEPTED
        else:
            data= {"msg": "Invalid credentials"}
            estado= status.HTTP_401_UNAUTHORIZED
        return Response(data,estado)
        
         
        # if user is not None:
        #     login(request, user)
        # Redirect to a success page.
        
        
        
class LogoutView(APIView):
    '''Logout usuario'''
    def post(self,request):
        email = request.data['email']
        try:
            user= CustomUser.objects.get(email=email)
            token= Token.objects.get(user=user)
            token.delete()
            mensaje= {"msg":"Successfully logged out"}
            estado= status.HTTP_200_OK

        except:
            mensaje= {"msg":"Invalid credentials"}
            estado= status.HTTP_401_UNAUTHORIZED
        return Response(mensaje,estado)


# Redirect to a success page.       