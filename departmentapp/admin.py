from django.contrib import admin
from .models import Department, Course, FormData


# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'department', 'name')


@admin.register(FormData)
class FormDataAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'department', 'course', 'purpose')
