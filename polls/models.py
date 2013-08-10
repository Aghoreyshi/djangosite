import datetime

from django.db import models
from django.utils import timezone
from django.forms import ModelForm


class Poll(models.Model):
    question = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    pub_date = models.DateTimeField('date published', auto_now_add=True,)

    def __unicode__(self):
        return self.question

    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    published_recently.boolean = True
    published_recently.admin_order_field = 'pub_date'


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
