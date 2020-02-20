"""Module to add Employee fields to the User admin interface."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Employee


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    max_num = 1
    verbose_name_plural = 'employee'
    

class UserAdmin(BaseUserAdmin):
    # Add the ssn, salary and last_updated fields to User admin view
    inlines = (EmployeeInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


