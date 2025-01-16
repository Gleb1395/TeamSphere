from datetime import datetime, timedelta
import random

from django.db import models
from faker import Faker

from worker.models import Worker


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
    objects = models.Manager()

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return f"{self.name} {self.start_date} {self.end_date} {self.status}"

    @staticmethod
    def create_test_project(count: int) -> None:
        fake = Faker()
        start_date = datetime.strptime(fake.date(), '%Y-%m-%d')

        for _ in range(count):
            Project.objects.create(
                name=f"{fake.word().capitalize()} {fake.word().capitalize()} Project",
                description=fake.text(max_nb_chars=50),
                start_date=start_date,
                end_date=start_date + timedelta(days=4),
                status=random.randint(0, 3),
            )


class Team(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    members = models.ManyToManyField(Worker, "members")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')
    objects = models.Manager()

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return f"{self.name}"

    @staticmethod
    def create_test_team(count: int) -> None:
        fake = Faker()
        project = Project.objects.all()
        worker = list(Worker.objects.all())

        if not project:
            raise ValueError("No projects, at least 1 is needed ")
        if not worker:
            raise ValueError("No workers, at least 1 is needed ")
        num_workers = random.randint(2, 5)
        selected_workers = random.sample(worker, min(num_workers, len(worker)))

        for _ in range(count):
            team = Team.objects.create(
                name=fake.word().capitalize(),
                description=fake.text(max_nb_chars=50),
                project=random.choice(project),
            )
            team.members.add(*selected_workers)
