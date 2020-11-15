from django.contrib.auth.models import User
from django.db import models
from datetime import date
import datetime


# Create your models here.


class TodoList(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=40, verbose_name="할일제목")
    description = models.TextField(max_length=200, verbose_name="할일세부사항")
    date_created = models.DateField(auto_now_add=True, verbose_name="생성날짜")
    date_deadline = models.DateField(verbose_name="데드라인")

    def remaining_days(self):
        delta = self.date_deadline - date.today()
        days = delta.days
        return days

    def __str__(self):
        return f'{self.name} | {self.description} | {self.date_created} | 		  {self.date_deadline}'
