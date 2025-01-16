from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from worker.models import Worker, Position


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)
