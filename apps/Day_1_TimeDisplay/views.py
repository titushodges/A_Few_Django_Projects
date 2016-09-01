from django.shortcuts import render, HttpResponse
import datetime
# Create your views here.
def index(request):
	now = {
    "time":datetime.datetime.now()
    }
	return render(request, 'Day_1_TimeDisplay/index.html', now)