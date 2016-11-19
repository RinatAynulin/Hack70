from django.db import models
from django.conf import settings

# Create your models here.

class GeneralModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(GeneralModel):
    parent = models.ForeignKey(
        'self', related_name='children',
        verbose_name=u'parent',
        blank=True, null=True,
    )
    content = models.TextField()
    post = models.ForeignKey('discussions.Post', related_name='post_comments')

    class Meta:
        verbose_name = u'Comment'
        verbose_name_plural = u'Comments'
        ordering = ('-created_at',)


    def __unicode__(self):
        return self.content

