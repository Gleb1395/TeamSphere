import random
from datetime import datetime

from django.db import models
from faker import Faker

from project.models import Project
from worker.models import Worker


class Task(models.Model):
    class Priority(models.IntegerChoices):
        HIGH = 2
        MEDIUM = 1
        LOW = 0

    name = models.CharField(max_length=120, unique=True)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.SmallIntegerField(choices=Priority.choices, default=Priority.LOW) # NOQA E501
    task_type = models.ForeignKey(
        "TaskType", on_delete=models.CASCADE, related_name="task"
    )
    assigned = models.ManyToManyField(Worker, related_name="assigned")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks") # NOQA E501
    objects = models.Manager()

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return f"{self.name} {self.is_completed} {self.priority} {self.task_type}" # NOQA E501

    @staticmethod
    def create_test_task(count: int) -> None:
        fake = Faker()
        worker = list(Worker.objects.all())
        projects = Project.objects.all()
        if not worker:
            raise ValueError("No workers, at least 1 is needed ")
        num_workers = random.randint(2, 5)
        selected_workers = random.sample(worker, min(num_workers, len(worker)))
        for _ in range(count):
            task = Task.objects.create(
                name=fake.name(),
                description=fake.text(max_nb_chars=50),
                deadline=datetime.now(),
                priority=random.randint(0, 2),
                project=random.choice(projects),
                task_type=TaskType.objects.create(name=f"{fake.name()} Task Type"), # NOQA E501
            )
            task.assigned.add(*selected_workers),


class TaskType(models.Model):
    name = models.CharField(max_length=120)
    objects = models.Manager()

    class Meta:
        verbose_name = "Task Type"
        verbose_name_plural = "Task Types"

    def __str__(self):
        return self.name
