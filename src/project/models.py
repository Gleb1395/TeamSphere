from django.db import models

from src.worker.models import Worker


class Project(models.Model):
    class Status(models.IntegerChoices):
        IN_PROGRESS = 0
        COMPLETED = 1
        ON_HOLD = 2
        CANCELLED = 3

    name = models.CharField(max_length=120)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.SmallIntegerField(
        choices=Status.choices,
        default=Status.IN_PROGRESS)


class Team(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    members = models.ManyToManyField(Worker)
    projects = models.ForeignKey(Project, on_delete=models.CASCADE)
