from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from project.models import Team
from worker.models import Worker


class WorkerCreateForm(UserCreationForm):
    teams = forms.ModelMultipleChoiceField(
        queryset=Team.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control",
            }
        ),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "pass",
                "placeholder": "Password",
            }
        ),
    )
    password2 = forms.CharField(
        label="Repeat Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "selectpicker form-control",
                "data-style": "py-0",
                "name": "type",
                "placeholder": "Confirm Password",
            }
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "country",
            "status",
            "phone_number",
            "position",
            "first_name",
            "last_name",
            "email",
            "password1",
        )
        widgets = {
            "position": forms.Select(
                attrs={
                    "class": "selectpicker form-control",
                    "data-style": "py-0",
                    "name": "type",
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": "selectpicker form-control",
                    "data-style": "py-0",
                    "name": "type",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "fname",
                    "placeholder": "First Name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "fname",
                    "placeholder": "Last Name",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "fname",
                    "placeholder": "Phone number",
                }
            ),
            "country": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "fname",
                    "placeholder": "Country",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "id": "email",
                    "type": "email",
                    "placeholder": "Email",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "uname",
                    "placeholder": "Username",
                    "type": "text",
                }
            ),
        }

    def save(self, commit=True):
        worker = super().save(commit=False)
        if commit:
            worker.save()
        worker.team.set(self.cleaned_data["teams"])
        return worker


class WorkerUpdateForm(UserChangeForm):
    teams = forms.ModelMultipleChoiceField(
        queryset=Team.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = Worker
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "country",
            "phone_number",
            "status",
        )
        widgets = {
            "position": forms.Select(
                attrs={
                    "class": "selectpicker form-control",
                    "data-style": "py-0",
                    "name": "type",
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": "selectpicker form-control",
                    "data-style": "py-0",
                    "name": "type",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "fname",
                    "placeholder": "First Name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "fname",
                    "placeholder": "Last Name",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "fname",
                    "placeholder": "Phone number",
                }
            ),
            "country": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "fname",
                    "placeholder": "Country",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "id": "email",
                    "type": "email",
                    "placeholder": "Email",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "uname",
                    "placeholder": "Username",
                    "type": "text",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "password" in self.fields:
            self.fields.pop("password")

    def save(self, commit=True):
        worker = super().save(commit=False)
        if commit:
            worker.save()
        worker.team.set(self.cleaned_data["teams"])
        return worker


class WorkerLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "floating-input form-control",
                "placeholder": "Username",
                "type": "text",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "floating-input form-control",
                "placeholder": "Password",
                "type": "password",
            }
        )
    )
