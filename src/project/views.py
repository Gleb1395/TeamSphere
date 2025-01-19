from django.urls import reverse_lazy
from django.views import generic

from project.forms import ProjectCreateForm, SearchForm
from project.models import Project
from worker.models import Worker


class ProjectListView(generic.ListView):
    model = Project
    template_name = "project/page_project.html"
    context_object_name = "projects"

    # paginate_by = 9 # ToDo implement this

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_status = [
            {"label": "In Progress", "value": Project.Status.IN_PROGRESS},
            {"label": "Completed", "value": Project.Status.COMPLETED},
            {"label": "On Hold", "value": Project.Status.ON_HOLD},
            {"label": "Cancelled", "value": Project.Status.CANCELLED},
        ]
        context["list_status"] = list_status

        search_text = self.request.GET.get("project_name", "")
        context["search_form"] = SearchForm(field=["project_name"], initial={"project_name": search_text})
        return context

    def get_queryset(self):
        # ToDo Implemented Q filter
        status_project = self.request.GET.get("status")
        if status_project:
            projects = Project.objects.filter(status=status_project)
            return projects
        name_project = self.request.GET.get("project_name", "")
        if name_project:
            name_project = name_project.strip()
            return Project.objects.filter(name__icontains=name_project)
        else:
            return Project.objects.all()


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = "project/project_detail.html"
    queryset = Project.objects.prefetch_related("teams")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status_color_mapping = [
            {"color_progress_bar": "primary", "value": 0},
            {"color_progress_bar": "secondary", "value": 1},
            {"color_progress_bar": "success", "value": 2},
            {"color_progress_bar": "danger", "value": 3},
        ]
        status_project = str(**kwargs).split()[0]
        color = "primary"
        for element in status_color_mapping:
            if element["value"] == int(status_project):
                color = element["color_progress_bar"]
                break
        context["color_for_progress"] = color

        project = Project.objects.prefetch_related("teams__members").get(pk=self.kwargs["pk"])
        worker = Worker.objects.filter(team__project=project)
        context["worker"] = worker

        return context


class ProjectCreateView(generic.CreateView):
    model = Project
    template_name = "project/project_create.html"
    form_class = ProjectCreateForm
    success_url = reverse_lazy("project:index")


class ProjectUpdateView(generic.UpdateView):
    model = Project
    template_name = "project/project_create.html"
    form_class = ProjectCreateForm
    success_url = reverse_lazy("project:index")


class ProjectDeleteView(generic.DeleteView):
    model = Project
    success_url = reverse_lazy("project:index")
    template_name = "project/project_confirm_delete.html"
