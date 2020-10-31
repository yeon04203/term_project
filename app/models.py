from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    user_test_point = models.IntegerField(default=0)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)


class Voca(models.Model):
    vid = models.IntegerField(blank=True)
    word = models.CharField(max_length=300)
    mean = models.CharField(max_length=300)
    grade = models.CharField(max_length=300)


class Today(models.Model):
    today_word = models.CharField(max_length=300)
    today_mean = models.CharField(max_length=300)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()