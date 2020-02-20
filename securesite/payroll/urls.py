from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/myinfo/', views.MyInfoView.as_view(), name='my_info'),
    path('api/v1/employee/<int:id>/', views.EmployeeView.as_view(), name='employee'),
    path('api/v1/employees/', views.EmployeesView.as_view(), name='employees'),
]