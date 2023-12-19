from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Department, FormData, Course


def form_data(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', )
        email = request.POST.get('email', )
        age = request.POST.get('age', )
        dob = request.POST.get('dob', )
        phone = request.POST.get('phone_number', )
        gender = request.POST.get('gender', )
        address = request.POST.get('address', )
        department = request.POST.get('department', )
        course_id = request.POST.get('course', )
        purpose = request.POST.get('purpose', )

        try:
            department_instance, created = Department.objects.get_or_create(name=department)
            course_instance, created = Course.objects.get_or_create(id=course_id)

            data = FormData(name=name, mail_id=email, age=age, dob=dob, phone_number=phone, gender=gender,
                            address=address,
                            department=department_instance, course=course_instance, purpose=purpose)
            data.save()
            messages.info(request, "Submission Successful!")
            return redirect('departmentapp:form')
        except:
            return redirect('departmentapp:form')

    return render(request, 'form_data.html', {'depart': departments})


def get_courses(request, department_id):
    courses = Course.objects.filter(department_id=department_id).values('id', 'name')
    return JsonResponse(list(courses), safe=False)
