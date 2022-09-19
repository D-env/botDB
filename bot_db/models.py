from django.db import models


# Create your models here.

class Member(models.Model):
    guild = models.IntegerField()
    hours = models.JSONField()
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name


class Event(models.Model):
    guild = models.IntegerField()
    title = models.CharField(max_length=256)
    description = models.TextField()
    time = models.DateTimeField()


