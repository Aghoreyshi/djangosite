import datetime

from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)

    def __unicode__(self):
        return self.title


class Entry(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True,)
    modified_date = models.DateTimeField('date last modified', auto_now=True,)
    categories = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.title

    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=7)

    published_recently.boolean = True
    published_recently.admin_order_field = 'pub_date'

    class Meta:
        ordering = ['pub_date']

