from django.urls import path,include
from authentication.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    
]