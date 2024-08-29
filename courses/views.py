from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Course
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import CourseMember
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def show_courses(request):
    courses_list = Course.objects.all()
    context = {'courses': courses_list}
    return render(request, 'courses/show.html', context)

def in_detail(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return HttpResponse("Course not found", status=404)
    return render(request, 'courses/show_more.html', {'course': course})

@login_required(login_url="/courses/login")
def rate(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method=="GET":
        return render(request, 'courses/rate.html', {'course': course})
    
    else:
        new_rating = request.POST.get('new_rate')
        course.rate = (course.rate*course.count + int(new_rating)) / (course.count + 1)
        course.count += 1
        course.save()
        return HttpResponseRedirect('/courses/')


def register(request):
    if request.method == "GET":
        return render(request, "courses/registration.html")
    
    firstname = request.POST['fname']
    lastname = request.POST['lname']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    age = request.POST['age']
    user = User.objects.create_user(first_name=firstname, 
                last_name=lastname, 
                username = username,
                password = password,
                email=email)
    user.save()
    member = CourseMember(user=user, age=int(age))
    member.save()
    return HttpResponseRedirect("/courses/login")


def login_into(request):
    if request.method == "GET":
        # next_url = request.GET.get('next')
        return render(request, "courses/login.html")
    
    
    usr = request.POST['username']
    pswd = request.POST['password']
    
    
    user = authenticate(username=usr, password=pswd)
    if user:
        login(request, user)
        return HttpResponseRedirect('/courses/')
    
    return render(request, "courses/login.html", {"error": "username or password is wrong"})