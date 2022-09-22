from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=256)
    guild = models.IntegerField(default=0)
    availability = models.JSONField()
    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    duration = models.IntegerField(default=0)
    guild = models.IntegerField(default=0)
    start_time = models.IntegerField(default=0)
    end_time = models.IntegerField(default=0)
    day = models.CharField(max_length=256)
    def __str__(self):
        return self.name