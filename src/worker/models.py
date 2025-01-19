import random

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from faker import Faker


class Worker(AbstractUser):
    class Status(models.IntegerChoices):
        ACTIVE = 1
        ON_LEAVE = 2
        TERMINATED = 3

    position = models.ForeignKey(
        "Position",
        on_delete=models.CASCADE,
        related_name="workers",
        null=True,
        blank=True,
    )
    country = models.CharField(max_length=100, null=True, blank=True)
    status = models.SmallIntegerField(choices=Status.choices, blank=True, default=Status.ACTIVE)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    objects = UserManager()

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"
        ordering = ["-id"]

    def __str__(self):
        return self.username

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
        list_country = [
            "Ukraine",
            "United Kingdom",
            "United States",
            "Germany",
            "Canada",
        ]
        for _ in range(count):
            position_name = random.choice(list_position)
            position, created = Position.objects.get_or_create(name=position_name)
            Worker.objects.create_user(
                username=fake.user_name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                password="password",
                position=position,
                country=random.choice(list_country),
                status=random.randint(1, 3),
                phone_number=fake.phone_number(),
            )


class Position(models.Model):
    name = models.CharField(
        max_length=120,
    )
    objects = models.Manager()

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"

    def __str__(self):
        return self.name
