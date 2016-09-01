from django.shortcuts import render, HttpResponse, redirect
import random
from django.contrib.sessions.models import Session
# Create your views here.
def index(request):
	if not request.session.get('gold') >=0:
		request.session['gold'] = 0
	if not request.session.get('z'):
		request.session['z'] = []
	stuff = {'z' : request.session['z']}
	return render(request, 'Day_3_Gold/index.html', stuff)

def process(request):
	
	if request.POST.get("val", "") == "farm":
		x = random.randint(11,21)
		request.session['gold'] += x
		y = "Earned {} gold from the farm!".format(x)
		request.session['z'].extend([y])
	elif request.POST.get("val", "") == "cave":
		x = random.randint(4,11)
		request.session['gold'] += x
		y = "Earned {} gold from the cave!".format(x)
		request.session['z'].extend([y])
	elif request.POST.get("val", "") == "house":
		x = random.randint(1,6)
		request.session['gold'] += x
		y = "Earned {} gold from the house!".format(x)
		request.session['z'].extend([y])
	else:
		x = random.randint(-51,51)
		request.session['gold'] += x
		y = "Earned {} gold from the casino!".format(x)
		request.session['z'].extend([y])
	return redirect('/ninjagold/',)

def reset(request):
	request.session.flush()
	return redirect('/ninjagold/')