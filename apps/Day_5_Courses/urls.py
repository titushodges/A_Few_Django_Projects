from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^create$', views.create),
	url(r'^courses/destroy/(?P<course_id>\d+)$', views.submit),
	url(r'^delete/(?P<course_id>\d+)$', views.delete),
	url(r'^user_courses$', views.user_courses),
	url(r'^user_create$', views.user_create),
]