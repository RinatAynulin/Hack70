# coding: utf-8

from __future__ import unicode_literals
from django.db.models import FileField, DateTimeField, TextField, ForeignKey, Model
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse

class Document(Model):
    file = FileField(upload_to='docs/', blank=False, null=False, verbose_name='Файл')
    description = TextField(max_length=1024, blank=False, verbose_name='Описание')
    created_at = DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = ForeignKey(settings.AUTH_USER_MODEL, related_name='files', verbose_name='Автор')
    comments = GenericRelation('comments.Comment', related_query_name='comments', verbose_name='Комментарии')


    class Meta:
        verbose_name = u'Фотокарточка'
        verbose_name_plural = u'Фотокарточки'
        ordering = ('-created_at',)