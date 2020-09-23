from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(blank=True)

class Voca(models.Model):
    vid=models.IntegerField(blank=True)
    word=models.CharField(max_length=300)
    mean=models.CharField(max_length=300)
    grade=models.CharField(max_length=300)