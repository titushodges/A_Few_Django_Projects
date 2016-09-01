from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^ninja$', views.ninja),
	url(r'^ninja/(?P<ninja_color>.*)$', views.turtle),
	url(r'^reset$', views.reset),
]