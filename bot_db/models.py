from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=256)
    guild = models.IntegerField()
    availability = models.JSONField()
    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    duration = models.IntegerField()
    guild = models.IntegerField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    day = models.CharField()