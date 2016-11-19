from django.conf import settings
from django.db import models


# Create your models here.

class GeneralModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey('courses.Course', related_name='posts')

    class Meta:
        abstract = True
