# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Day_7_Login', '0003_auto_20160830_1418'),
        ('Day_5_Courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='users',
            field=models.ManyToManyField(related_name='course', to='Day_7_Login.users'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=models.TextField(),
        ),
    ]
