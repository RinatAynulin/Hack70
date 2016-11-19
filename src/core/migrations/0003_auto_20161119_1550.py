# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Student', 'Студент'), ('Teacher', 'Преподаватель')], max_length=25, verbose_name='должность'),
        ),
    ]
