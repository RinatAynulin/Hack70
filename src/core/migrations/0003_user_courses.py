# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('core', '0002_auto_20161120_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='courses',
            field=models.ManyToManyField(related_name='members', to='courses.Course'),
        ),
    ]
