from django.contrib import admin
from django.urls import path, include
from .views import UpdateEmployeeInfoView, GetAllEmployeesView, GetEmployeesDivisionsDetailsView, DeleteEmployeeView, CreateNewEmployeeView

urlpatterns = [
    path('get-all-employees', GetAllEmployeesView.as_view()),
    path('create-new-employee', CreateNewEmployeeView.as_view()),
    path('update-info/<int:pk>', UpdateEmployeeInfoView.as_view()),
    path('delete-employee/<int:pk>', DeleteEmployeeView.as_view()),
    path('get-divisions-details', GetEmployeesDivisionsDetailsView.as_view())
]

