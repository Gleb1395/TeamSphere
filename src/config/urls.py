from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("project.urls", namespace="project")),
    path("worker/", include("worker.urls", namespace="worker")),
    # path("", include("task.urls", namespace="task")),
]
