from django.db import models


# Create your models here.


class GeneralModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()  # link to chair at mipt.ru

    def __unicode__(self):
        return self.title

    class Meta:
        abstract = True


class Chair(GeneralModel):
    class Meta:
        verbose_name = u'Chair'
        verbose_name_plural = u'Chairs'


class Course(GeneralModel):
    chair = models.ForeignKey(Chair, related_name='chair_courses')
    class Meta:
        verbose_name = u'Course'
        verbose_name_plural = u'courses'
