from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth  import authenticate,login,logout
from django.contrib import messages
def index(request):
    return render(request,"index.html")
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
def teacher_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)

        try:
            teacher = Teacher.objects.get(email=email, password=password)  # Check if teacher exists
            request.session['teacher_id'] = teacher.id  # Store teacher ID in session
            messages.success(request, "Teacher Login Successful")
            return redirect('teacher_home')  # Redirect to teacher's dashboard
        except Teacher.DoesNotExist:
            messages.error(request, "Invalid Teacher Email or Password")
            return redirect('teacher_login')

    return render(request, 'teacher_login.html')


def student_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            student = Student.objects.get(email=email, password=password)  # Check if student exists
            request.session['student_id'] = student.id  # Store student ID in session
            messages.success(request, "Student Login Successful")
            return redirect('student_home')  # Redirect to student's dashboard
        except Student.DoesNotExist:
            messages.error(request, "Invalid Student Email or Password")
            return redirect('student_login')

    return render(request, 'student_login.html')

def admim_superadmin_login(request):

    if request.method=='POST':
        
        u=request.POST['uname']
        p=request.POST['pswd']
        
        user=auth.authenticate(username=u,password=p)
        try:
            if user.is_staff:
                # print("Inside  ")
                auth.login(request,user)
                messages.success(request,"Login Successfull")
                return redirect('superuser_home')
            
            elif user is not None:
                auth.login(request,user)
                messages.success(request,"Login Successfull")
                return redirect('admin_home')
            
            else:
              
                messages.error(request,"Some error occurred")
        except:
            messages.error(request,"Invalid Login Credentials")
         
    
    return render(request, 'login.html',)

   
def admin_home(request):
    return render(request, 'admin_home.html')
   
def superuser_home(request):
    return render(request, 'superuser_home.html')

def teacher_home(request):
    return render(request,'teacher_home.html')

def student_home(request):
    return render(request,'student_home.html')