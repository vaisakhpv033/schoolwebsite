# urls.py

from django.urls import path
from .views import form_data, get_courses

app_name = 'departmentapp'

urlpatterns = [
    path('form/', form_data, name='form'),
    path('get-courses/<int:department_id>/', get_courses, name='get_courses'),
]
