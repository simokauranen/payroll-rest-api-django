from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import permissions
from django.contrib.auth.models import User

from . import models
from . import serializers


class MyInfoView(APIView):
    """
        APiView class to regular employee to view his/her own information.
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        """ Get employee information with the user_id in employee's own credentials 
            (id in auth_user table)
        """
        employee = models.Employee.objects.filter(user_id=request.user.id)
        if employee.count() == 0: # This might happen, if User does not have Employee fields
            return Response({ 'Error': 'Employee not found'})
        serialized_employee = serializers.EmployeeSerializer(employee, many=True)
        return Response({ 'employee': serialized_employee.data})
        
        


class EmployeeView(APIView):
    """
        APiView class to admin user to view and modify employee's information.
    """
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def get(self, request, id):
        """Get employee information with the id in auth_user table"""
        employee = models.Employee.objects.filter(user_id=id)
        if employee.count() == 0: # This might happen, if User does not have Employee fields
            return Response({ 'Error': 'Employee not found'})
        serialized_employee = serializers.EmployeeSerializer(employee, many=True)
        return Response({ 'employee': serialized_employee.data})


    def post(self, request, id):
        """Update employee information (salary)"""

        employee = models.Employee.objects.filter(user_id=id).first()
        if employee == None:
            return Response({ 'Error': 'Employee not found'})

        new_salary = request.POST.get('salary')
        if new_salary != None:
            serialized_employee = serializers.EmployeeSerializer(
                employee, 
                data={'salary': new_salary},
                partial=True
            )

            if serialized_employee.is_valid():
                serialized_employee.save(employee)
                return Response({ 'employee': serialized_employee.data})
            else:
                return Response({ 'Error': 'Parameters not valid'})
        else:
            serialized_employee = serializers.EmployeeSerializer(employee)
            return Response({  'Error': 'Employee not updated'})

class EmployeesView(APIView):
    """
        APiview class to admin user to view the info of all employees.
    """
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        """Return info of all employees"""
        employees = models.Employee.objects.all()
        if employees.count() == 0:
            return Response({ 'Error': 'Employees not found'})
        serialized_employees = serializers.EmployeeSerializer(employees, many=True)
        return Response({ 'employees': serialized_employees.data})
