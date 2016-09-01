from __future__ import unicode_literals
from django.db import models
from ..Day_7_Login.models import users

class CourseManager(models.Manager):
    def add_user_to_course(self, form_data):
        course = self.get(id=form_data['course'])
        user = users.objects.get(id=form_data['user'])
        course.user1.add(user)
        course.save()

class courses(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
    user1 = models.ManyToManyField('Day_7_Login.users', related_name='course')