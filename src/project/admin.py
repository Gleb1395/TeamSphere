from django.contrib import admin

from project.models import Project, Team


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date", "status")


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name",)
