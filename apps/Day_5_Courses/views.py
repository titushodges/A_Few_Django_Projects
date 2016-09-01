from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Count
from .models import courses
from ..Day_7_Login.models import users
# Create your views here.
def index(request):
	courses1 = courses.objects.all()
	context = {'courses':courses1}
	return render(request, 'Day_5_Courses/index.html', context)

def create(request):
	name = request.POST['name']
	desc = request.POST['desc']
	courses.objects.create(course_name=name,description=desc)
	return redirect('/courses/')

def submit(request, course_id):
	courses1 = courses.objects.filter(id=course_id)
	context = {'courses':courses1}
	return render(request, 'Day_5_Courses/submit.html', context)

def delete(request, course_id):
	courses.objects.filter(id=course_id).delete()
	return redirect('/courses/')

def user_courses(request):
	context = {
        'users' : users.objects.all(),
        'courses' : courses.objects.annotate(students=Count('user1')),
    }
	return render(request, 'Day_5_Courses/courses.html', context)

def user_create(request):
	courses.objects.add_user_to_course(request.POST)
	return redirect('/courses/user_courses')