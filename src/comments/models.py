# coding: utf-8

from django.conf import settings
from django.db import models
from django.db.models import TextField, DateTimeField, ForeignKey, Model, PositiveIntegerField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class Comment(Model):
    author = ForeignKey(settings.AUTH_USER_MODEL, blank=False, related_name='comments', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name=u'дата изменения')

    content_type = ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    comments = GenericRelation('comments.Comment', related_name = 'comments')

    text = TextField(blank=False, max_length=1024, verbose_name='комментарий')


    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return '%i by %s' % (self.content_object.id, self.author)