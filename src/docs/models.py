# coding: utf-8

from __future__ import unicode_literals
from django.db.models import FileField, DateTimeField, TextField, ForeignKey, Model, CharField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse

class Document(Model):
    title = CharField(max_length=255, blank=False, verbose_name='Название')
    file = FileField(upload_to='docs/', blank=False, null=False, verbose_name='Файл')
    description = TextField(max_length=1024, blank=False, verbose_name='Описание')
    created_at = DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = ForeignKey(settings.AUTH_USER_MODEL, related_name='files', verbose_name='Автор')
    votes = GenericRelation('votes.Vote', related_name='votes')
    comments = GenericRelation('comments.Comment', related_name = 'comments')



    class Meta:
        verbose_name = u'Фотокарточка'
        verbose_name_plural = u'Фотокарточки'
        ordering = ('-created_at',)