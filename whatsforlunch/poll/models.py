from django.db import models
from whatsforlunch.account.models import User


class Poll(models.Model):

    candidates = models.ManyToManyField()
    start       = models.DateTimeField()
    end         = models.DateTimeField()
    voters      = models.ManyToManyField()

    class Meta:
        db_table = 'poll'


class Vote(models.Model):

    user        = models.ForeignKey(User)
    poll        = models.ForeignKey(Poll)
    choice      = models.ForeignKey()

    class Meta:
        db_table = 'vote'