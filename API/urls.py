from django.contrib import admin
from django.urls import path, include
from .views import UpdateView, GetView, SaveView, DeleteView, Join

urlpatterns = [
    path('get/', GetView.as_view()),
    path('save/', SaveView.as_view()),
    path('update/<int:pk>', UpdateView.as_view()),
    path('delete/<int:pk>', DeleteView.as_view()),
    path('employees/subdivision/', Join.as_view())
]

