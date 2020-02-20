from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    ssn = models.CharField(max_length=11)
    salary = models.FloatField()
    last_updated = models.DateTimeField()
    
    


