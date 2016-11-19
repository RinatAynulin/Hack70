from django.conf import settings
from django.db import models
from django.db.models import TextField, DateTimeField, ForeignKey, Model, PositiveIntegerField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

VOTE_TYPES = (
    (1, 'UP'),
    (-1, 'DOWN'),
)

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    vote_type = models.IntegerField(choices=VOTE_TYPES)

    content_type = ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # post = models.ForeignKey('discussions.Post')

    class Meta:
        unique_together = (('user', 'object_id', 'content_type'),)
        verbose_name = 'Vote'
        verbose_name_plural = 'Votes'

    def __str__(self):
        return '{} {} was voited {} by {}'.format(self.content_type, self.object_id, self.vote_type, self.user.username)

