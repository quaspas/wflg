from django.db import models
from whatsforlunch.account.models import User


class Poll(models.Model):

    restaurants = models.ManyToManyField()
    start       = models.DateTimeField()
    end         = models.DateTimeField()
    voters      = models.ManyToManyField()

    class Meta:
        db_table = 'poll'


# you do not need an account to vote. only to make a poll.
# so votes are cast by IP address? by cookie?

class Vote(models.Model):

    user        = models.ForeignKey(User)
    poll        = models.ForeignKey(Poll)
    choice      = models.ForeignKey(Restaurant)

    class Meta:
        db_table = 'vote'


class Restaurant(models.Model):

    name        = models.CharField()
    location    = models.CharField()

    class Meta:
        db_table = 'restaurant'