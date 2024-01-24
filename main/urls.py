from django.urls import path
from .views import EmployeeListAPI, EmployeeDetailAPI

urlpatterns = [
    path('', EmployeeListAPI, name='EmployeeListAPI'),
    path('EmployeeDetailAPI/<int:employee_id>', EmployeeDetailAPI, name='EmployeeDetailAPI'),
]
