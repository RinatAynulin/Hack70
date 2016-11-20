# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

from courses.models import Course


class User(AbstractUser):
    avatar = models.ImageField(u'фото профиля',upload_to='avatars', blank=False, default=u'avatars/default-avatar.jpg')
    first_name = models.CharField(u'имя', max_length=30, blank=False)
    last_name = models.CharField(u'фамилия', max_length=30, blank=False)
    email = models.EmailField(u'e-mail', blank=False, unique=True)

    permission = models.IntegerField(default=0) #0 - student, 1 - prep and so on

    USER_TYPE = ((None, u'Ваша должность'), (u'Студент', u'Студент'), (u'Преподаватель', u'Преподаватель'))
    user_type = models.CharField(u'должность', choices=USER_TYPE, max_length=25, blank=False)

    courses = models.ManyToManyField(Course, related_name='members')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('core:user', kwargs={'slug': self.username})


