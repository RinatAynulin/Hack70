from django.db import models
from django.conf import settings
from comments.models import Comment
from votes.models import Vote
from django.contrib.contenttypes.fields import GenericRelation


class GeneralModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    votes = GenericRelation('votes.Vote', related_name='votes')
    comments = GenericRelation('comments.Comment', related_name='comments')

    class Meta:
        abstract = True


class Post(GeneralModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey('courses.Course', related_name='course_posts')

    class Meta:
        verbose_name = u'Post'
        verbose_name_plural = u'Posts'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def score(self):
        from django.contrib.contenttypes.models import ContentType
        return Vote.objects.filter(object_id=self.pk).filter(content_type=ContentType.objects.get_for_model(self)) \
                   .aggregate(models.Sum('vote_type')).get('vote_type__sum') or 0

    def comments_count(self):
        return Comment.objects.filter(post=self).count()


class News(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_news")
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey('courses.Course', related_name='course_news')

