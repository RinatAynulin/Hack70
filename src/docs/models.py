# coding: utf-8
from __future__ import unicode_literals
from django.db.models import FileField, DateTimeField, TextField, ForeignKey, Model, CharField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from comments.models import Comment
from votes.models import Vote
from django.db import models
from django.contrib.contenttypes.models import ContentType


class Document(Model):
    title = CharField(max_length=255, blank=False, verbose_name='Название')
    file = FileField(upload_to='docs/', blank=False, null=False, verbose_name='Файл')
    description = TextField(max_length=1024, blank=False, verbose_name='Описание')
    created_at = DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = ForeignKey(settings.AUTH_USER_MODEL, related_name='files', verbose_name='Автор')
    votes = GenericRelation('votes.Vote', related_name='votes')
    comments = GenericRelation('comments.Comment', related_name = 'comments')
    course = models.ForeignKey('courses.Course', related_name='course_docs', verbose_name='Курс')


    class Meta:
        verbose_name = u'Документ'
        verbose_name_plural = u'Документы'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def score(self):
        from django.contrib.contenttypes.models import ContentType
        return Vote.objects.filter(object_id=self.pk).filter(content_type=ContentType.objects.get_for_model(self)) \
                   .aggregate(models.Sum('vote_type')).get('vote_type__sum') or 0

    def comments_count(self):
        return Comment.objects.filter(object_id=self.pk).filter(content_type=ContentType.objects.get_for_model(self)).count()