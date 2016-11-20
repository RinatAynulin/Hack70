# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 06:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
                ('object_id', models.PositiveIntegerField()),
                ('text', models.TextField(max_length=1024, verbose_name='комментарий')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'Комментарии',
                'verbose_name': 'Комментарий',
                'ordering': ('-created_at',),
            },
        ),
    ]
