from django.db import models

from src.worker.models import Worker


class Task(models.Model):
    class Priority(models.IntegerChoices):
        HIGH = 2
        MEDIUM = 1
        LOW = 0

    name = models.CharField(max_length=120, unique=True)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.SmallIntegerField(
        choices=Priority.choices,
        default=Priority.LOW
    )
    task_type = models.ForeignKey(
        "TaskType",
        on_delete=models.CASCADE,
        related_name="task"
    )
    assigned = models.ManyToManyField(Worker, related_name='assigned')
    project = models.ForeignKey(...)  # ToDo Added this models field


class TaskType(models.Model):
    name = models.CharField(max_length=120)
