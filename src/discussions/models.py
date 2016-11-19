from django.db import models
from django.conf import settings

# Create your models here.
from comments.models import Comment
from votes.models import PostVote


class GeneralModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey('courses.Course', related_name='course_posts')


class Post(GeneralModel):
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        verbose_name = u'Post'
        verbose_name_plural = u'Posts'
        ordering = ('-created_at',)


    def __str__(self):
        return self.title

    def score(self):
        return PostVote.objects.filter(post=self).aggregate(models.Sum('vote_type')).get('vote_type__sum') or 0

    def comments_count(self):
        return Comment.objects.filter(post=self).count()
