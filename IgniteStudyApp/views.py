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
        username = request.POST.get('uname')
        password = request.POST.get('password')
      

        try:
            teacher = Teacher.objects.get(name=username, password=password)  # Check if teacher exists
            request.session['teacher_id'] = teacher.id  # Store teacher ID in session
            messages.success(request, "Teacher Login Successful")
            return redirect('teacher_home')  # Redirect to teacher's dashboard
        except Teacher.DoesNotExist:
            messages.error(request, "Invalid Teacher Email or Password")
            return redirect('teacher_login')

    return render(request, 'teacher/teacher_login.html')


def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pswd')
        

        try:
            student = Student.objects.get(name=username, password=password)  # Check if student exists
            request.session['student_id'] = student.id  # Store student ID in session
            print("id")
            messages.success(request, "Student Login Successful")
            print("Redirectign")
            return redirect('student_home')  # Redirect to student's dashboard
        except Student.DoesNotExist:
            print(Student.DoesNotExist)
            messages.error(request, "Invalid Student Email or Password")
            return redirect('student_login')

    return render(request, 'student/student_login.html')

def manager_superadmin_login(request):

    if request.method=='POST':
        
        u=request.POST['uname']
        p=request.POST['password']
        print(u)
        print(p)
        
        user=auth.authenticate(username=u,password=p)
        try:
            if user.is_staff:
                print("Inside superadmin ")
                auth.login(request,user)
                messages.success(request,"Login Successfull")
                return redirect('superuser_home')
            
            elif user is not None:
                print("Insideadmin")
                auth.login(request,user)
                messages.success(request,"Login Successfull")
                return redirect('manager_home')
            
            else:
              
                messages.error(request,"Some error occurred")
        except Exception as e:
            print(e)
            messages.error(request,"Invalid Login Credentials")
         
    
    return render(request, 'manager/manager_superadmin_login.html',)

   
def manager_home(request):
    return render(request, 'manager/manager_home.html')
   
def superuser_home(request):
    return render(request, 'superadmin/superuser_home.html')

def teacher_home(request):
    return render(request,'teacher/teacher_home.html')

def student_home(request):
    return render(request,'student/student_home.html')