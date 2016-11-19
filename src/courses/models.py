from django.db import models


# Create your models here.


class GeneralModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()  # link to chair at mipt.ru

    def __unicode__(self):
        return self.title


class Chair(GeneralModel):
    pass


class Course(GeneralModel):
    chair = models.ForeignKey(Chair, related_name='courses')
