from django.urls import path

from project.views import (ProjectCreateView, ProjectDeleteView,
                           ProjectDetailView, ProjectListView,
                           ProjectUpdateView)

urlpatterns = [
    path("", ProjectListView.as_view(), name="index"),
    path("<int:status>", ProjectListView.as_view(), name="index_with_status"),
    path("project-detail/<int:pk>", ProjectDetailView.as_view(), name="project-detail"),  # NOQA E501
    path("project-create", ProjectCreateView.as_view(), name="project-create"),
    path("project-update/<int:pk>", ProjectUpdateView.as_view(), name="project-update"),  # NOQA E501
    path("project-delete/<int:pk>", ProjectDeleteView.as_view(), name="project-delete"),  # NOQA E501
]
app_name = "project"
