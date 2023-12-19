from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('departmentapp:form')
        else:
            messages.info(request, '*Invalid credentials')
            return redirect('schoolapp:login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']

        try:
            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username already taken!")
                    return redirect('schoolapp:register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email already taken!")
                    return redirect('schoolapp:register')
                else:
                    user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                    last_name=last_name, email=email)
                    user.save();
                    print('user created')
                    return redirect('schoolapp:login')
            else:
                messages.info(request, "Passwords not matching!")
                return redirect('schoolapp:register')
        except:
            messages.info(request, "Please fill the details before submitting!")
            return redirect('schoolapp:register')
    return render(request, 'home.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
