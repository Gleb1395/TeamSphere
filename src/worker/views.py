from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic

from project.forms import SearchForm
from worker.forms import WorkerCreateForm, WorkerLoginForm, WorkerUpdateForm
from worker.models import Worker


class WorkerListView(generic.ListView):
    model = Worker
    context_object_name = "workers"
    # paginate_by = 10
    template_name = "templates/worker/worker_list.html"
    queryset = Worker.objects.prefetch_related("team")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status_worker = [
            {"color": "primary", "value": 1},
            {"color": "secondary", "value": 2},
            {"color": "success", "value": 3},
        ]
        context["status_worker"] = status_worker

        search_text = self.request.GET.get("worker_name", "")
        context["search_form"] = SearchForm(field=["worker_name"], initial={"worker_name": search_text})

        return context


class WorkerCreateView(generic.CreateView):
    model = Worker
    template_name = "templates/worker/worker_create.html"
    form_class = WorkerCreateForm
    success_url = reverse_lazy("worker:worker-list")


class WorkerUpdateView(generic.UpdateView):
    model = Worker
    template_name = "templates/worker/worker_update.html"
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("worker:worker-list")


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("worker:worker-list")
    template_name = "worker/worker_confirm_delete.html"


class WorkerDetailView(generic.DetailView):
    model = Worker
    template_name = "templates/worker/worker_detail.html"


class WorkerRegistrationView(generic.CreateView):
    model = Worker
    template_name = "templates/worker/worker_sign_up.html"
    form_class = WorkerCreateForm
    success_url = reverse_lazy("worker:worker-list")

    def form_valid(self, form):
        response = super().form_valid(form)
        worker = self.object
        login(self.request, worker)
        return response


class WorkerLoginView(LoginView):
    model = Worker
    template_name = "templates/worker/worker_sign_in.html"
    success_url = reverse_lazy("worker:worker-list")
    form_class = WorkerLoginForm

    def form_valid(self, form):
        return super().form_valid(form)


class WorkerLogoutView(LogoutView):
    next_page = reverse_lazy("project:index")
