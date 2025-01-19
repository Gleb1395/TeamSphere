from django import forms

from project.models import Project


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "start_date", "end_date", "status"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "exampleInputText01",
                    "placeholder": "Project Name",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "exampleInputText01",
                    "placeholder": "Description project",
                }
            ),
            "start_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                    "id": "exampleInputText04",
                    "placeholder": "Start Date",
                }
            ),
            "end_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                    "id": "exampleInputText04",
                    "placeholder": "End Date",
                }
            ),
            "status": forms.Select(
                attrs={
                    "name": "type",
                    "class": "selectpicker form-control",
                    "data-style": "py-0",
                }
            ),
        }

    # ToDo Added validation for start date


class SearchForm(forms.Form):
    project_name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "text search-input",
                "placeholder": "Search by project",
            }
        ),
    )

    worker_name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "text search-input",
                "placeholder": "Search by name worker",
            }
        ),
    )

    def __init__(self, *args, field=None, **kwargs):
        super().__init__(*args, **kwargs)
        if field is not None:
            for key in list(self.fields.keys()):
                if key not in field:
                    del self.fields[key]
