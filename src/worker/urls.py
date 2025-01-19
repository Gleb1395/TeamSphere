from django.urls import path

from .views import (WorkerCreateView, WorkerDeleteView, WorkerDetailView,
                    WorkerListView, WorkerLoginView, WorkerLogoutView,
                    WorkerRegistrationView, WorkerUpdateView)

app_name = "worker"

urlpatterns = [
    path("worker-list/", WorkerListView.as_view(), name="worker-list"),
    path("worker-create/", WorkerCreateView.as_view(), name="worker-create"),
    path("worker-update/<int:pk>", WorkerUpdateView.as_view(), name="worker-update"),
    path("worker-delete/<int:pk>", WorkerDeleteView.as_view(), name="worker-delete"),
    path("worker-detail/<int:pk>", WorkerDetailView.as_view(), name="worker-detail"),
    path("sign-up/", WorkerRegistrationView.as_view(), name="sign-up"),
    path("sign-in/", WorkerLoginView.as_view(), name="sign-in"),
    path("logout", WorkerLogoutView.as_view(), name="logout"),
]
