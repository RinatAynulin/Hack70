from django.conf import settings
from django.db import models

VOTE_TYPES = (
    (1, 'UP'),
    (-1, 'DOWN'),
)

class PostVote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey('discussions.Post')
    vote_type = models.IntegerField(choices=VOTE_TYPES)

    def __unicode__(self):
        return 'User: {} \n Post: {} \n Vote: {}'.format(self.user.username, self.post.title, self.vote_type)


class CommentVote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.ForeignKey('comments.Comment') #fixme foreign key
    vote_type = models.IntegerField(choices=VOTE_TYPES)

    def __unicode__(self):
        return 'User: {} \n Comment: {} \n Vote: {}'.format(self.user.username, self.post.title, self.vote_type)