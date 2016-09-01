from django.shortcuts import render, HttpResponse, redirect
import datetime, uuid
from django.contrib.sessions.models import Session
# Create your views here.
def index(request):
	return render(request, 'Day_3_DisNinjas/index.html')

def ninja(request):
	request.session['ninja'] = False
	return render(request, 'Day_3_DisNinjas/ninja.html')

def turtle(request, ninja_color):
	request.session['ninja'] = False
	request.session['blue'] = False
	request.session['orange'] = False
	request.session['red'] = False
	request.session['purple'] = False
	request.session['megan'] = False
	if ninja_color == 'blue':
		request.session['ninja'] = True
		request.session['blue'] = True
	elif ninja_color == 'orange':
		request.session['ninja'] = True
		request.session['orange'] = True
	elif ninja_color == 'red':
		request.session['ninja'] = True
		request.session['red'] = True
	elif ninja_color == 'purple':
		request.session['ninja'] = True
		request.session['purple'] = True
	else:
		request.session['ninja'] = True
		request.session['megan'] = True
	return render(request, 'Day_3_DisNinjas/ninja.html')

def reset(request):
	request.session.flush()
	return redirect('/ninjas/ninja')