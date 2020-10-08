from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)


class Voca(models.Model):
    vid = models.IntegerField(blank=True)
    word = models.CharField(max_length=300)
    mean = models.CharField(max_length=300)
    grade = models.CharField(max_length=300)
    like = models.ManyToManyField(User, related_name='likes', blank=True)


class Today(models.Model):
    today_word = models.CharField(max_length=300)
    today_mean = models.CharField(max_length=300)
