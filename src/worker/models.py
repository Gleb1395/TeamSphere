import random

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from faker import Faker


class Worker(AbstractUser):
    position = models.ForeignKey("Position",
                                 on_delete=models.CASCADE,
                                 related_name="workers",
                                 null=True,
                                 blank=True
                                 )
    objects = UserManager()

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

    @staticmethod
    def create_test_worker(count: int) -> None:
        fake = Faker()
        list_position = [
            "QA Engineer",
            "Backend Developer",
            "Frontend Developer",
            "DevOps Engineer",
            "UI/UX Designer",
        ]
        for _ in range(count):
            Worker.objects.create_user(
                username=fake.user_name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                password="password",
                position=Position.objects.create(
                    name=random.choice(list_position),
                )
            )


class Position(models.Model):
    name = models.CharField(max_length=120, )
    objects = models.Manager()

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"

    def __str__(self):
        return self.name
