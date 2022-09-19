from django.db import models
import jsonfield

# Create your models here.

class Member(models.Model):
    guild = models.IntegerField(required=True)
    hours = jsonfield.JSONField(required=True)
    name = models.CharField(max_length=256, required=True)
    def __str__(self):
        return self.name


class Event(models.Model):
    guild = models.IntegerField(required=True)
    title = models.CharField(max_length=256, required=True)
    description = models.TextField(required=True)
    time = models.DateTimeField(required=True)


