from .models import Employee
from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils import timezone 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', )



class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, required=True)

    class Meta:
        model = Employee
        fields = ('user', 'ssn', 'salary', 'last_updated', )

    def save(self, instance):
        instance.last_updated = timezone.now() # The salary was just updated
        super().save()

        
